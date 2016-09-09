#! /usr/bin/python

# 21_from_interleaved_to_sequential.py

# transform a interleaved fasta file into a sequential format fasta file

# Jie Wang
# September 7, 2016

import argparse
import os.path
import sys


parser = argparse.ArgumentParser(description = 'transform a interleaved fasta '
                                               'file into a sequential format '
                                               'fasta file')

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
FILE_OUT = open(outputFile, 'w')
flag = True

while True:
    line = FILE_IN.readline()
    if not line:
        break
    # counter here to get rid of the first line empty issue
    if flag:
        FILE_OUT.write('{0}'.format(line))
        flag = False
    else:
        if line.startswith('>'):
            FILE_OUT.write('\n{0}\n'.format(line.rstrip()))
        else:
            FILE_OUT.write(line.rstrip())

# print(counter)

FILE_IN.close()
FILE_OUT.close()