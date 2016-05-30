#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cPickle as pickle
import bz2
import json
import argparse

def transform_json_to_pkl(args):
    with open(args.json_input, 'r') as json_file:
        json_str = json_file.read()
        metadata = json.loads(json_str)

        for marker in metadata["markers"]:
            metadata["markers"][marker]["ext"] = set(metadata["markers"][marker]["ext"])

    pkl_output = bz2.BZ2File(args.pkl_output, 'w')
    pickle.dump(metadata, pkl_output, pickle.HIGHEST_PROTOCOL)
    pkl_output.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--json_input', required=True)
    parser.add_argument('--pkl_output', required=True)
    
    args = parser.parse_args()

    transform_json_to_pkl(args)
