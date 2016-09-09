#! /usr/bin/python

# 23_find_NP_regex.py

# find the fasta header contains NP in the text. Write the sequence and
# accession ID to the new fasta file using regex

# Jie Wang
# September 7, 2016

import argparse
import os.path
import sys
import re


parser = argparse.ArgumentParser(description = 'find the fasta header contains NP in the text. '
                                               'Write the sequence and accession ID to the new fasta file')

parser.add_argument('-i', '--input', help='input fasta data',
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

FILE_IN=open(inputFile, 'r')
FILE_OUT=open(outputFile, 'w')

seqDict={}
firstLine=True

while True:
    line=FILE_IN.readline()
    if not line:
        break

    if line.startswith('>'):
        flagNP=0
        matchStr = re.split('\|', line)

        # determine if Accession number existed
        if matchStr[3].startswith('NP'):
            if firstLine:
                FILE_OUT.write('>{0}\n'.format(matchStr[3]))
                firstLine=False
            else:
                FILE_OUT.write('\n>{0}\n'.format(matchStr[3]))
            flagNP=1
        # the continue permits read the next line
        continue

    if flagNP==1:
        FILE_OUT.write(line.rstrip())

FILE_OUT.write('\n')

FILE_IN.close()
FILE_OUT.close()