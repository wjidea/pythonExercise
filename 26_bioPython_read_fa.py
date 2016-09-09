#! /usr/bin/python

# 26_biopython_read_fa.py

# read fasta formatted file using biopython module

import argparse
import os.path
import sys
from Bio import SeqIO


parser = argparse.ArgumentParser(description = 'biopython read fasta'
                                               'and print to terminal')

parser.add_argument('-i', '--input', help='input fasta data',
                    required = True)
parser.add_argument('-v', '--verbose', help = 'increase verbosity',
                    action = 'store_true')
args = parser.parse_args()

# check if the input fild existed
inputFile = args.input

filesL = [inputFile]

if args.verbose:
    # check file path one at a time and tell which one is missing
    for inputFile in filesL:
        if not os.path.isfile(inputFile):
            print('Input file {} does not exist!'.format(inputFile))
            sys.exit()
else:
    # check file path in a bulk, but may not be the optimum case
    if not all(map(os.path.isfile, filesL)):
        print('Missing input file(s)!')
        sys.exit()

# ABOVE are all HEADER INFO

faGenerator = SeqIO.parse(inputFile, 'fasta')
for seq in faGenerator:
    print('Sequence ID: {}'.format(seq.id))
    print('Sequence length: {}'.format(len(seq)))
    print('Sequence description: {}'.format(seq.description))
    print(seq.seq)
    print('\n')
