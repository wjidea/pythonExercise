#! /usr/bin/python

# 25_genotype_swap.py

# transform a genotype file by making the Fn generation individuals consistent
# with their parental generation labels

import argparse
import os.path
import sys


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

FILE_IN = open(inputFile, 'r')

# read all lines into a list
matrix = [line.rstrip().split('\t') for line in FILE_IN]

# define the dimension of the matrix
numOfRow = len(matrix)
numOfCol = len(matrix[0])

for row in range(1,numOfRow):
    if matrix[row][1] == 'A':
        continue
    else:
        for col in range(1,numOfCol):
            if matrix[row][col] == 'A':
                matrix[row][col] = 'B'
            elif matrix[row][col] == 'B':
                matrix[row][col] = 'A'

# obtain a column col 1 should be all A's
# col1 = [row[1] for row in matrix]

FILE_IN.close()


# write the matrix to a file
FILE_OUT = open(outputFile, 'w')

FILE_OUT.writelines('\t'.join(i) + '\n' for i in matrix)

FILE_OUT.close()