#! /usr/bin/python

# 22_2_find_the_NP.py

# find the fasta header contains NP in the text. Write the sequence and
# accession ID to the new fasta file

# Jie Wang
# September 7, 2016


import itertools
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



# credit to code monk

def find_gene_ID(file, gene_id):
    '''
    :param file:  file handle
    :param gene_id: initial gene ID to look for [str]
    :return: gene ID and sequence [dict]
    '''
    for header,group in itertools.groupby(file, lambda x: x.startswith('>')):
        if header:
            line = group.next()
            word = re.split('\|', line)
            ncbi_id = word[3]

        elif ncbi_id.startswith(gene_id):
            sequence = ''.join(line.strip() for line in group)
            yield ncbi_id, sequence

if __name__ == '__main__':

    FILE_IN = open(inputFile, 'r')
    FILE_OUT = open(outputFile, 'w')

    allNpSeqs = dict(find_gene_ID(FILE_IN, 'NP'))

    # print(len(allNpSeqs))
    for accID in allNpSeqs:
        if accID.startswith('NP'):
            seq = allNpSeqs[accID]
            FILE_OUT.write('>{0}\n{1}\n'.format(accID, seq))


    FILE_IN.close()
    FILE_OUT.close()