#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re

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
                for i in range(len(more_abund_charact)-1,-1,-1):
                    if abundances[more_abund_charact[i]] < abund:
                        best_pos = i
                    else:
                        break
                if best_pos != None:
                    tmp_more_abund_charact = more_abund_charact
                    more_abund_charact = tmp_more_abund_charact[:best_pos]
                    more_abund_charact += [charact_id]
                    more_abund_charact += tmp_more_abund_charact[best_pos:-1]
    return abundances, more_abund_charact

def format_characteristic_name(all_name):
    if all_name.find(':') != -1:
        charact_id = all_name.split(':')[0]
        charact_name = all_name.split(':')[1][1:]
    else:
        charact_id = all_name
        charact_name = ''

    charact_name = charact_name.replace('/',' ')
    charact_name = charact_name.replace('-',' ')
    charact_name = charact_name.replace("'",'')
    if charact_name.find('(') != -1 and charact_name.find(')') != -1:
        open_bracket = charact_name.find('(')
        close_bracket = charact_name.find(')')+1
        charact_name = charact_name[:open_bracket] + charact_name[close_bracket:]
    return charact_id,charact_name

def write_more_abundant_charat(abundances,more_abund_charact, output_filepath):
    with open(output_filepath,'w') as output_file:
        output_file.write('id\tname\t')
        output_file.write('\t'.join(abundances.keys()) + '\n')

        for mac in more_abund_charact:
            charact_id,charact_name = format_characteristic_name(mac)
            output_file.write(charact_id + '\t' + charact_name)
            for sample in abundances:
                abund = abundances[sample].get(mac, 0)
                output_file.write('\t' + str(abund))
            output_file.write('\n')

def extract_similar_characteristics(abundances, sim_output_filepath,
    specific_output_files):
    sim_characteristics = set(abundances[abundances.keys()[0]].keys())
    for sample in abundances.keys()[1:]:
        sim_characteristics.intersection_update(abundances[sample].keys())
    print 'Similar between all samples:', len(sim_characteristics)

    with open(sim_output_filepath, 'w') as sim_output_file:
        sim_output_file.write('id\tname\t' + '\t'.join(abundances.keys()) + '\n')
        for charact in list(sim_characteristics):
            charact_id,charact_name = format_characteristic_name(charact)
            sim_output_file.write(charact_id + '\t' + charact_name)
            for sample in abundances.keys():
                sim_output_file.write('\t' + str(abundances[sample][charact]))
            sim_output_file.write('\n')

    print 'Specific to samples:'
    diff_characteristics = {}
    for i in range(len(abundances.keys())):
        sample = abundances.keys()[i]
        print ' ', sample, ""
        print '    All:', len(abundances[sample].keys())
        diff_characteristics[sample] = set(abundances[sample].keys())
        diff_characteristics[sample].difference_update(sim_characteristics)
        print '    Number of specific characteristics:', 
        print len(diff_characteristics[sample])
        print '    Percentage of specific characteristics:',
        print 100*len(diff_characteristics[sample])/(1.*len(abundances[sample].keys()))

        relative_abundance = 0
        with open(specific_output_files[i], 'w') as output_file:
            output_file.write('id\tname\tabundances\n')
            for charact in list(diff_characteristics[sample]):
                charact_id,charact_name = format_characteristic_name(charact)
                output_file.write(charact_id + '\t' + charact_name + '\t')
                output_file.write(str(abundances[sample][charact]) + '\n')
                relative_abundance += abundances[sample][charact]
        print '    Relative abundance of specific characteristics(%):', relative_abundance

    return sim_characteristics

def compare_humann2_output(args):
    abundances = {}
    more_abund_charact = []

    for i in range(len(args.sample_name)):
        abundances[args.sample_name[i]], mac = extract_abundances(args.charact_input_file[i],
            args.most_abundant_characteristics_to_extract)
        more_abund_charact += mac

    write_more_abundant_charat(abundances, list(set(more_abund_charact)), 
        args.more_abundant_output_file)
    sim_characteristics = extract_similar_characteristics(abundances, 
        args.similar_output_file, args.specific_output_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--sample_name', required=True, action='append')
    parser.add_argument('--charact_input_file', required=True, action='append')
    parser.add_argument('--most_abundant_characteristics_to_extract', required=True,
        type = int)
    parser.add_argument('--more_abundant_output_file', required=True)
    parser.add_argument('--similar_output_file', required=True)
    parser.add_argument('--specific_output_file', required=True,action='append')
    args = parser.parse_args()

    if len(args.sample_name) != len(args.charact_input_file):
        raise ValueError("Same number of values (in same order) are expected for --sample_name and --charact_input_file")
    if len(args.sample_name) != len(args.specific_output_file):
        raise ValueError("Same number of values (in same order) are expected for --sample_name and --specific_output_file")

    compare_humann2_output(args)