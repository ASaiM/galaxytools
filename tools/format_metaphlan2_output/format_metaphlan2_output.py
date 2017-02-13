#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse


taxo_level_correspondance = {}
taxo_level_correspondance['k'] = 'kingdom'
taxo_level_correspondance['p'] = 'phylum'
taxo_level_correspondance['c'] = 'class'
taxo_level_correspondance['o'] = 'order'
taxo_level_correspondance['f'] = 'family'
taxo_level_correspondance['g'] = 'genus'
taxo_level_correspondance['s'] = 'species'
taxo_level_correspondance['t'] = 'strains'


def write_taxo_abundance(output_files, level, taxo, abundance):
    if level not in taxo_level_correspondance:
        raise ValueError(level + ' is not a know taxonomic level')
    output_files[taxo_level_correspondance[level]].write(taxo + '\t')
    output_files[taxo_level_correspondance[level]].write(abundance + '\n')


def format_metaphlan2_output(args):
    taxo_levels_abund_files = {}
    taxo_levels_abund_files['kingdom'] = open(args.kingdom_abundance_file, 'w')
    taxo_levels_abund_files['phylum'] = open(args.phylum_abundance_file, 'w')
    taxo_levels_abund_files['class'] = open(args.class_abundance_file, 'w')
    taxo_levels_abund_files['order'] = open(args.order_abundance_file, 'w')
    taxo_levels_abund_files['family'] = open(args.family_abundance_file, 'w')
    taxo_levels_abund_files['genus'] = open(args.genus_abundance_file, 'w')
    taxo_levels_abund_files['species'] = open(args.species_abundance_file, 'w')
    taxo_levels_abund_files['strains'] = open(args.strains_abundance_file, 'w')

    for taxo_level_file in taxo_levels_abund_files:
        string = taxo_level_file + '\t' + 'abundance\n'
        taxo_levels_abund_files[taxo_level_file].write(string)

    with open(args.metaphlan2_output, 'r') as input_file:
        with open(args.all_taxo_level_abundance_file, 'w') as output_file:
            string = "kingdom\t"
            string += "phylum\t"
            string += "class\t"
            string += "order\t"
            string += "family\t"
            string += "genus\t"
            string += "species\t"
            string += "strains\t"
            string += "abundance\n"
            output_file.write(string)

            levels_number = 8
            for line in input_file.readlines():
                if line.startswith("#"):
                    continue

                split_line = line[:-1].split('\t')
                all_taxo = split_line[0]
                abundance = split_line[1]

                split_taxo = all_taxo.split('|')
                for level in split_taxo:
                    taxo = level.split('__')[1]
                    taxo = taxo.replace("_", " ")
                    output_file.write(taxo + '\t')

                for i in range(len(split_taxo), levels_number):
                    output_file.write('\t')

                output_file.write(abundance + "\n")

                last_taxo_level = split_taxo[-1].split('__')
                taxo = last_taxo_level[1].replace("_", " ")
                level = last_taxo_level[0]
                write_taxo_abundance(
                    taxo_levels_abund_files,
                    level,
                    taxo,
                    abundance)

    for taxo_level_file in taxo_levels_abund_files:
        taxo_levels_abund_files[taxo_level_file].close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--metaphlan2_output', required=True)
    parser.add_argument('--all_taxo_level_abundance_file', required=True)
    parser.add_argument('--kingdom_abundance_file', required=True)
    parser.add_argument('--phylum_abundance_file', required=True)
    parser.add_argument('--class_abundance_file', required=True)
    parser.add_argument('--order_abundance_file', required=True)
    parser.add_argument('--family_abundance_file', required=True)
    parser.add_argument('--genus_abundance_file', required=True)
    parser.add_argument('--species_abundance_file', required=True)
    parser.add_argument('--strains_abundance_file', required=True)
    args = parser.parse_args()

    format_metaphlan2_output(args)
