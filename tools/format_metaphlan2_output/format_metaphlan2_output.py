#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re

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
    if not taxo_level_correspondance.has_key(level):
        raise ValueError(level + ' is not a know taxonomic level')
    output_files[taxo_level_correspondance[level]].write(taxo + '\t')
    output_files[taxo_level_correspondance[level]].write(abundance + '\n')

def format_metaphlan2_output(args):
    taxo_levels_abundance_files = {}
    taxo_levels_abundance_files['kingdom'] = open(args.kingdom_abundance_file, 'w')
    taxo_levels_abundance_files['phylum'] = open(args.phylum_abundance_file, 'w')
    taxo_levels_abundance_files['class'] = open(args.class_abundance_file, 'w')
    taxo_levels_abundance_files['order'] = open(args.order_abundance_file, 'w')
    taxo_levels_abundance_files['family'] = open(args.family_abundance_file, 'w')
    taxo_levels_abundance_files['genus'] = open(args.genus_abundance_file, 'w')
    taxo_levels_abundance_files['species'] = open(args.species_abundance_file, 'w')
    taxo_levels_abundance_files['strains'] = open(args.strains_abundance_file, 'w')

    for taxo_level_file in taxo_levels_abundance_files:
        taxo_levels_abundance_files[taxo_level_file].write(taxo_level_file + '\t')
        taxo_levels_abundance_files[taxo_level_file].write('abundance\n')

    with open(args.metaphlan2_output, 'r') as input_file:
        with open(args.all_taxo_level_abundance_file, 'w') as output_file:
            output_file.write("kingdom\t")
            output_file.write("phylum\t")
            output_file.write("class\t")
            output_file.write("order\t")
            output_file.write("family\t")
            output_file.write("genus\t")
            output_file.write("species\t")
            output_file.write("strains\t")
            output_file.write("abundance\n")
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
                    taxo = taxo.replace("_"," ")
                    output_file.write(taxo + '\t')

                for i in range(len(split_taxo), levels_number):
                    output_file.write('\t')

                output_file.write(abundance + "\n")


                last_taxo_level = split_taxo[-1].split('__')
                taxo = last_taxo_level[1].replace("_"," ")
                level = last_taxo_level[0]
                write_taxo_abundance(taxo_levels_abundance_files, level, taxo, 
                    abundance)

    for taxo_level_file in taxo_levels_abundance_files:
        taxo_levels_abundance_files[taxo_level_file].close()

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