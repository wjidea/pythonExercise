#! /usr/bin/python

# 22_find_the_NP.py

# find the fasta header contains NP in the text. Write the sequence and
# accession ID to the new fasta file

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

FILE_IN = open(inputFile, 'r')

counter = 0
seqDict = {}

while True:
    line=FILE_IN.readline()
    if not line:
        break
    if line.startswith('>'):
        matchStr = re.match(r'>gi\|\d+\|\w+\|([\w\d\.]*)', line)
        # determine if Accession number existed
        if matchStr:
            accessionNum = matchStr.group(1)
        # otherwise, rename it with Group_
        else:
            accessionNum = 'Group_{}'.format(counter)
            counter += 1
        seqDict[accessionNum] = ""
        continue
    seqDict[accessionNum] += line.rstrip()
FILE_IN.close()


FILE_OUT=open(outputFile, 'w')
for accID in seqDict:
    if accID.startswith('NP'):
        seq = seqDict[accID]
        FILE_OUT.write('>{0}\n{1}\n'.format(accID, seq))
FILE_OUT.close()