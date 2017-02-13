#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse


def write_seq_fasta_format(seq, output_file):
    split_seq = [seq[i:i+60] for i in range(0, len(seq), 60)]
    for split in split_seq:
        output_file.write(split + '\n')


def fasta_add_barcode(args):
    mapping = {}
    with open(args.input_mapping_file, 'r') as input_mapping_file:
        for line in input_mapping_file:
            split_line = line[:-1].split('\t')

            if len(split_line) != 2:
                string = 'Incorrect number of column in mapping file.'
                string += '\nTwo tabular separated columns are expected'
                raise ValueError(string)

            mapping[split_line[0]] = split_line[1]

    seq_id = ''
    seq = ''
    with open(args.input_sequence_file, 'r') as input_sequence_file:
        with open(args.output_sequence_file, 'w') as output_sequence_file:
            for line in input_sequence_file:
                if line.startswith('>'):
                    if seq != '':
                        if seq_id not in mapping:
                            string = 'A sequence identifier (' + seq_id
                            string += ') is not found in mapping file'
                            raise ValueError(string)

                        output_sequence_file.write('>' + seq_id + '\n')

                        barcode = mapping[seq_id]
                        seq = barcode + seq
                        write_seq_fasta_format(seq, output_sequence_file)
                    seq_id = line[1:-1].split()[0]
                    seq = ''
                else:
                    seq += line[:-1]

########
# Main #
########
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_sequence_file', required=True)
    parser.add_argument('--input_mapping_file', required=True)
    parser.add_argument('--output_sequence_file', required=True)
    args = parser.parse_args()

    fasta_add_barcode(args)
