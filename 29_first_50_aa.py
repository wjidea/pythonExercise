#! /usr/bin/python

# 29_first_50_aa.py

# truncate the first 50 amino acids from each sequence in fasta

import argparse
import os.path
import sys
from Bio import SeqIO

parser = argparse.ArgumentParser(description = 'swap genotypes to make it '
                                               'consistent with their parental'
                                               'generations')

parser.add_argument('-i', '--input', help='input genotype data',
                    required = True)
parser.add_argument('-o', '--output', help = 'output file in text format',
                    required = True)
parser.add_argument('-v', '--verbose', help = 'increase verbosity',
                    action = 'store_true')
args = parser.parse_args()

# check if the input fild existed
inputFile = args.input
outputFile = args.output

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
if os.path.isfile(outputFile):
    print('output file {0} already exists'.format(outputFile))
    sys.exit()

# ABOVE are all HEADER INFO

faSeqGenerator = SeqIO.parse(inputFile, 'fasta')

FILE_OUT = open(outputFile, 'w')

for seqRec in faSeqGenerator:
    newSeqRec = seqRec
    newSeqRec.seq = seqRec.seq[0:50]
    newSeqRec.id = seqRec.id+'50aa|'
    newSeqRec.description = 'partial sequence '+\
                            ''.join(seqRec.description.split()[1:])+\
                            ' - first 50 aa'
    # print(newSeqRec.description)
    SeqIO.write(seqRec, FILE_OUT, 'fasta')

FILE_OUT.close()
