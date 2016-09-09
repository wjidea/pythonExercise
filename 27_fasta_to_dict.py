#! /usr/bin/python

# 27_fasta_to_dict.py

# read fasta formatted file using biopython module and store them in dict

import argparse
import os.path
import sys
from Bio import SeqIO

parser = argparse.ArgumentParser(description = 'read fasta formatted file using '
                                               'biopython module and store them '
                                               'in dict')

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

faSeqDict = SeqIO.to_dict(SeqIO.parse(inputFile, 'fasta'))

for seqRec in faSeqDict:
    print('Sequence ID: {}'.format(seqRec))
    print('Sequence length: {}'.format(len(faSeqDict[seqRec])))
    # print('\n')
