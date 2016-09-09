#! /usr/bin/python

# 28_sort_sort_by_size.py

# read fasta formatted file using biopython module and store them in dict

import argparse
import os.path
import sys
from Bio import SeqIO

parser = argparse.ArgumentParser(description = 'swap genotypes to make it '
                                               'consistent with their parental'
                                               'generations')

parser.add_argument('-i', '--input', help='input fasta data',
                    required = True)
parser.add_argument('-b', '--bigoutput', help = 'output file in text format',
                    required = True)
parser.add_argument('-s', '--smalloutput', help = 'output file in text format',
                    required = True)
parser.add_argument('-v', '--verbose', help = 'increase verbosity',
                    action = 'store_true')
args = parser.parse_args()

# check if the input fild existed
inputFile = args.input
outputBigFile = args.bigoutput
outputSmallFile = args.smalloutput

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

# check if output file is present
if os.path.isfile(outputBigFile):
    print('output file {0} already exists'.format(outputBigFile))
    sys.exit()

# check if output file is present
if os.path.isfile(outputSmallFile):
    print('output file {0} already exists'.format(outputSmallFile))
    sys.exit()

# ABOVE are all HEADER INFO
faSeqGenerator = SeqIO.parse(inputFile, 'fasta')

FILE_OUT_BIG = open(outputBigFile, 'w')
FILE_OUT_SMALL = open(outputSmallFile, 'w')

for seqRec in faSeqGenerator:
    if len(seqRec) > 300:
        SeqIO.write(seqRec, FILE_OUT_BIG, 'fasta')
    else:
        SeqIO.write(seqRec, FILE_OUT_SMALL, 'fasta')

FILE_OUT_BIG.close()
FILE_OUT_SMALL.close()
