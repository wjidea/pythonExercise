#! /usr/bin/python

# 24_extract_evalue_blasy.py

# blast populus transcript against arabdopsis transcript and extract evalue
# from blast resulsts.

# cmd line and parameters

# formatdb  -i Arabidopsis_thaliana_transcripts.fasta -n arab_nuc
# -p F -t arab_nuc

# -i input file path
# -n base name for blast file/ index file?
# -p type of input file F = nucleotide
# -t title for the database

# blastall -b 100 -v 100 -p blastn -d arab_nuc -a 12
# -i Populus_tremuloides.mRNA.PUT_filtered.fasta -o ara_v_pop_blastn_results.txt

# -b number of database alignements to show
# -v Number of database sequences to show one-line descriptions
# -p program name
# -d database
# -i input query sequence file
# -o blast results output
# -a number of threads


# extract the query name nad the hits with Evalue less than 10-e4
# 1) find the query line first, extract the first part of the query sequence,
#    save the query sequence as dict key
# 2) find the one description line 'Sequences producing significant alignments'
#    append the significant results to the dict items


# Jie Wang
# September 7, 2016


import re
import argparse
import os.path
import sys


parser = argparse.ArgumentParser(description = 'parse BLAST output and find '
                                               'e value less than 1e-10')

parser.add_argument('-i', '--input', help='input BLAST file in default format',
                    required = True)
parser.add_argument('-o', '--output', help = 'output file in text format',
                    required = True)
parser.add_argument('-e', '--evalue', help = 'cutoff evalue threshold',
                    type = float, default = 1e-10)
parser.add_argument('-v', '--verbose', help = 'increase verbosity',
                    action = 'store_true')
args = parser.parse_args()

# check if the input fild existed
inputFile = args.input
outputFile = args.output
evalueThreshold = float(args.evalue)

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


# Functions - subroutine
def evalueFilter(onelineDesc, filter):
    '''
    Function to compare evalue
    :param onelineDesc: one-line description in BLAST output[str]
    :param filter: evalue threshold can be scientific notation [float]
    :return: logical [True/False]
    '''

    #parse one-line description
    linedescMatch = re.match(r'\s([\d\.e\-]{1,})$', onelineDesc.rstrip())
    evalueStr = linedescMatch.group(1)

    # E-value is a fixed length col, len = 5 char
    # e.g. Evalue = e-108, which misses the 1 at the start
    if evalueStr.startswith('e'):
        evalueStr = '1'+evalueStr
        evalue = float(evalueStr)
    else:
        evalue = float(evalueStr)
    return(evalue <= filter)

def parseQuery(queryLine): # return query Key [str]
    '''
    Function to parse the query line to get query key
    :param queryLine: query line obtain from BLAST file
    :return: query ID
    '''
    if not queryLine.startswith('Query= '):
        return('Error! No query message.')
    queryID = queryLine.split()[1]
    return(queryID)


# open BLAST output file
FILE_IN = open(inputFile, 'r')

# claim list and dict names
hitsDict = {}
queryKey = ''
hitDescL = []

# start the program
while True:
    line = FILE_IN.readline()
    if not line:
        break

    # parse the query line
    if line.startswith('Query= '):
        queryStr = line
        while True:
            lineQ = FILE_IN.readline().rstrip()
            if not lineQ:
                break
            queryStr = queryStr + lineQ

        queryKey = parseQuery(queryStr)

    # parse the one-line description block
    if line.startswith('Sequences producing significant alignments:'):

        _ = FILE_IN.readline() # skip one line
        lineDesc = FILE_IN.readline() # assign first hit to lineDesc

        while True:
            if lineDesc in ['\n', '\r\n']:
                break

            # determine if pass evalue threshold
            passEvalue = evalueFilter(lineDesc, evalueThreshold)

            if passEvalue:
                # print(lineDesc.rstrip())
                hitDescL.append(lineDesc.rstrip())

            else:
                break
            lineDesc = FILE_IN.readline()
        # print(hitDescL)
    # assign one-line description to dict
        if hitDescL:
            hitsDict[queryKey] = hitDescL
            hitDescL = []
        # print(hitsDict)

FILE_IN.close()



# write parse blast output
FILE_OUT = open(outputFile, 'w')

sortDictKey = sorted(hitsDict.keys())

# possible improvement, sort by the last four numeric digits

for queryID in sortDictKey:
    FILE_OUT.write('Query= {}\n'.format(queryID))
    for hit in hitsDict[queryID]:
        FILE_OUT.write('{}\n'.format(hit))
    FILE_OUT.write('\n')
FILE_OUT.close()

