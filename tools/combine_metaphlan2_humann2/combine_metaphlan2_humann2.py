#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse


def extract_clade_abundance(metaphlan2_filepath):
    clade_abundance = {}
    with open(metaphlan2_filepath, 'r') as metaphlan2_file:
        for line in metaphlan2_file.readlines():
            if line.find('g__') == -1:
                continue

            split_line = line[:-1].split('\t')
            taxo = split_line[0]
            abundance = split_line[1]

            genus = taxo[(taxo.find('g__')+3):]
            if genus.find('|') != -1:
                genus = genus[:(genus.find('|'))]
            clade_abundance.setdefault(genus, {'abundance': 0, 'species': {}})
            if taxo.find('t__') != -1:
                continue
            elif taxo.find('s__') != -1:
                species = taxo[(taxo.find('s__')+3):]
                clade_abundance[genus]['species'].setdefault(
                    species,
                    abundance)
            else:
                clade_abundance[genus]['abundance'] = abundance
    return clade_abundance


def compute_overall_abundance(humann2_file):
    overall_abundance = 0
    with open(args.humann2_file, 'r') as humann2_file:
        for line in humann2_file.readlines():
            if line.find('|') != -1 or line.startswith('#'):
                continue
            split_line = line[:-1].split('\t')
            overall_abundance += float(split_line[1])
    return overall_abundance


def format_characteristic_name(name):
    format_name = name
    format_name = format_name.replace('/', ' ')
    format_name = format_name.replace('-', ' ')
    format_name = format_name.replace("'", '')
    if format_name.find('(') != -1 and format_name.find(')') != -1:
        open_bracket = format_name.find('(')
        close_bracket = format_name.find(')')+1
        format_name = format_name[:open_bracket] + format_name[close_bracket:]
    return format_name


def combine_metaphlan2_humann2(args):
    clade_abundance = extract_clade_abundance(args.metaphlan2_file)
    overall_abundance = compute_overall_abundance(args.humann2_file)

    with open(args.output_file, 'w') as output_file:
        string = 'genus\t'
        string += 'genus_abundance\t'
        string += 'species\t'
        string += 'species_abundance\t'
        string += args.type + '_id\t'
        string += args.type + '_name\t'
        string += args.type + '_abundance\n'
        output_file.write(string)
        with open(args.humann2_file, 'r') as humann2_file:
            for line in humann2_file.readlines():
                if line.find('|') == -1:
                    continue

                split_line = line[:-1].split('\t')
                abundance = 100*float(split_line[1])/overall_abundance
                annotation = split_line[0].split('|')
                characteristic = annotation[0].split(':')
                characteristic_id = characteristic[0]
                char_name = ''
                if len(characteristic) > 1:
                    char_name = format_characteristic_name(characteristic[-1])
                taxo = annotation[1].split('.')

                if taxo[0] == 'unclassified':
                    continue
                genus = taxo[0][3:]
                species = taxo[1][3:]

                if genus not in clade_abundance:
                    print("no" + genus + "found in" + args.metaphlan2_file)
                    continue
                if species not in clade_abundance[genus]['species']:
                    string = "no" + species + "found in" + args.metaphlan2_file
                    string += "for" + genus
                    print(string)
                    continue
                string = genus + '\t'
                string += clade_abundance[genus]['abundance'] + '\t'
                string += species + '\t'
                string += clade_abundance[genus]['species'][species] + '\t'
                string += characteristic_id + '\t'
                string += char_name + '\t'
                string += str(abundance) + '\n'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--humann2_file', required=True)
    parser.add_argument('--metaphlan2_file', required=True)
    parser.add_argument('--output_file', required=True)
    parser.add_argument(
        '--type',
        required=True,
        choices=['gene_families', 'pathways'])
    args = parser.parse_args()

    combine_metaphlan2_humann2(args)
