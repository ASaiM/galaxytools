#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse


def extract_abundances(filepath, nb_charact_to_extract):
    abundances = {}
    more_abund_charact = []
    abund_sum = 0
    with open(filepath, 'r') as abundance_file:
        for line in abundance_file.readlines()[1:]:
            split_line = line[:-1].split('\t')
            charact_id = split_line[0]
            abund = float(split_line[1])
            abundances[charact_id] = 100*abund
            abund_sum += abundances[charact_id]

            if len(more_abund_charact) < nb_charact_to_extract:
                more_abund_charact.append(charact_id)
            else:
                best_pos = None
                for i in range(len(more_abund_charact)-1, -1, -1):
                    if abundances[more_abund_charact[i]] < abund:
                        best_pos = i
                    else:
                        break
                if best_pos is not None:
                    tmp_more_abund_charact = more_abund_charact
                    more_abund_charact = tmp_more_abund_charact[:best_pos]
                    more_abund_charact += [charact_id]
                    more_abund_charact += tmp_more_abund_charact[best_pos:-1]
    return abundances, more_abund_charact


def format_characteristic_name(all_name):
    if all_name.find(':') != -1:
        charact_id = all_name.split(':')[0]
        char_name = all_name.split(':')[1][1:]
    else:
        charact_id = all_name
        char_name = ''

    char_name = char_name.replace('/', ' ')
    char_name = char_name.replace('-', ' ')
    char_name = char_name.replace("'", '')
    if char_name.find('(') != -1 and char_name.find(')') != -1:
        open_bracket = char_name.find('(')
        close_bracket = char_name.find(')')+1
        char_name = char_name[:open_bracket] + char_name[close_bracket:]
    return charact_id, char_name


def write_more_abundant_charat(abundances, more_abund_charact,
                               output_filepath):
    with open(output_filepath, 'w') as output_file:
        output_file.write('id\tname\t')
        output_file.write('\t'.join(abundances.keys()) + '\n')

        for mac in more_abund_charact:
            charact_id, charact_name = format_characteristic_name(mac)
            output_file.write(charact_id + '\t' + charact_name)
            for sample in abundances:
                abund = abundances[sample].get(mac, 0)
                output_file.write('\t' + str(abund))
            output_file.write('\n')


def extract_similar_characteristics(abund, sim_output_filepath,
                                    specific_output_files):
    sim_characteristics = set(abund[abund.keys()[0]].keys())
    for sample in abund.keys()[1:]:
        sim_characteristics.intersection_update(abund[sample].keys())
    print('Similar between all samples:' + str(len(sim_characteristics)))

    with open(sim_output_filepath, 'w') as sim_output_file:
        sim_output_file.write('id\tname\t' + '\t'.join(abund.keys()) + '\n')
        for charact in list(sim_characteristics):
            charact_id, charact_name = format_characteristic_name(charact)
            sim_output_file.write(charact_id + '\t' + charact_name)
            for sample in abund.keys():
                sim_output_file.write('\t' + str(abund[sample][charact]))
            sim_output_file.write('\n')

    print('Specific to samples:')
    diff_char = {}
    for i in range(len(abund.keys())):
        sample = abund.keys()[i]
        string = ' ' + sample + ""
        string += '    All:' + len(abund[sample].keys())
        diff_char[sample] = set(abund[sample].keys())
        diff_char[sample].difference_update(sim_characteristics)
        string += '    Number of specific characteristics:'
        string += str(len(diff_char[sample]))
        string += '    Percentage of specific characteristics:',
        perc = 100*len(diff_char[sample])/(1.*len(abund[sample].keys()))
        string += str(perc)
        print(string)

        relative_abundance = 0
        with open(specific_output_files[i], 'w') as output_file:
            output_file.write('id\tname\tabundances\n')
            for charact in list(diff_char[sample]):
                charact_id, charact_name = format_characteristic_name(charact)
                output_file.write(charact_id + '\t' + charact_name + '\t')
                output_file.write(str(abund[sample][charact]) + '\n')
                relative_abundance += abund[sample][charact]
        string = '    Relative abundance of specific characteristics('
        string += relative_abundance
        string += '):'
        print(string)

    return sim_characteristics


def compare_humann2_output(args):
    abundances = {}
    more_abund_charact = []

    for i in range(len(args.sample_name)):
        abundances[args.sample_name[i]], mac = extract_abundances(
            args.charact_input_file[i],
            args.most_abundant_characteristics_to_extract)
        more_abund_charact += mac

    write_more_abundant_charat(
        abundances,
        list(set(more_abund_charact)),
        args.more_abundant_output_file)
    extract_similar_characteristics(
        abundances,
        args.similar_output_file,
        args.specific_output_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--sample_name', required=True, action='append')
    parser.add_argument('--charact_input_file', required=True, action='append')
    parser.add_argument(
        '--most_abundant_characteristics_to_extract',
        required=True,
        type=int)
    parser.add_argument('--more_abundant_output_file', required=True)
    parser.add_argument('--similar_output_file', required=True)
    parser.add_argument(
        '--specific_output_file',
        required=True,
        action='append')
    args = parser.parse_args()

    if len(args.sample_name) != len(args.charact_input_file):
        string = "Same number of values (in same order) are expected for "
        string += "--sample_name and --charact_input_file"
        raise ValueError(string)
    if len(args.sample_name) != len(args.specific_output_file):
        string = "Same number of values (in same order) are expected for "
        string += "--sample_name and --specific_output_file"
        raise ValueError(string)

    compare_humann2_output(args)
