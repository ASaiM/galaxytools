#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re

reago_dir = '/tools/rna_manipulation/reago/reago/'

def add_read_pair_num(input_filepath, output_filepath, read_pair_num):
    to_add = '.' + str(read_pair_num)
    with open(input_filepath,'r') as input_file:
        with open(output_filepath,'w') as output_file:
            for line in input_file:
                if line[0] == '>':
                    split_line = line.split()
                    seq_id = split_line[0]
                    if seq_id.rfind(to_add) != (len(seq_id)-len(to_add)):
                        split_line[0] = seq_id + to_add
                    output_file.write(' '.join(split_line) + '\n')
                else:
                    output_file.write(line)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--r1_sequence_file', required=True)
    parser.add_argument('--r2_sequence_file', required=True)
    args = parser.parse_args()

    add_read_pair_num(args.r1_sequence_file, args.r1_sequence_file, 1)
    add_read_pair_num(args.r2_sequence_file, args.r2_sequence_file, 2)