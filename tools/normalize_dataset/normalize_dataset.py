#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def normalize_dataset(args):
    with open(args.input_file, 'r') as input_file:
        input_file_content = input_file.readlines()
        if args.normalization == 'column':
            column_number = len(input_file_content[0][:-1].split('\t'))
            column_sum = [0] * column_number

        with open(args.output_file, 'w') as output_file:
            for line in input_file_content:
                split_line = line[:-1].split('\t')

                if args.normalization == 'row':
                    row_sum = 0

                    for col in split_line:
                        if isfloat(col):
                            row_sum += float(col)

                    sep = ''
                    string = ''
                    for col in split_line:
                        if isfloat(col):
                            prop = float(col)/row_sum
                            if args.format == 'percentage':
                                string += sep + str(100*prop)
                            else:
                                string += sep + str(prop)
                        else:
                            string += sep + col
                        sep = '\t'
                    output_file.write(string + '\n')

                elif args.normalization == 'column':
                    for i in range(len(split_line)):
                        if isfloat(split_line[i]):
                            column_sum[i] += float(split_line[i])

            if args.normalization == 'column':
                for line in input_file_content:
                    split_line = line[:-1].split('\t')
                    string = ''
                    sep = ''
                    for i in range(len(split_line)):
                        if isfloat(split_line[i]):
                            prop = float(split_line[i])/column_sum[i]
                            if args.format == 'percentage':
                                string += sep + str(100*prop)
                            else:
                                string += sep + str(prop)
                        else:
                            string += sep + split_line[i]
                        sep = '\t'
                    output_file.write(string + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', required=True)
    parser.add_argument('--output_file', required=True)
    parser.add_argument(
        '--normalization',
        required=True,
        choices=['column', 'row'])
    parser.add_argument(
        '--format',
        required=True,
        choices=['proportion', 'percentage'])
    args = parser.parse_args()
    normalize_dataset(args)
