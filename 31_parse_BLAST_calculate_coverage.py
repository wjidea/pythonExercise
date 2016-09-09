#! /usr/bin/python

# 31_parse_BLAST_calculate_coverage.py

# blast populus transcript against arabdopsis transcript and extract evalue
# from blast resulsts (plain text) using biopython SearchIO.

# requirements for this script
# Write the output as Tab-delimited file, which includes:
# 1) Name of the Query sequence qResult.id
# 2) name of the best hit sequence hit.
# 3) percent identity for the alignment
# 4) percent coverage for the alignment
# 5) condition: percent identity > 70% percent coverage > 80%


import argparse
import os.path
import sys
from Bio import SearchIO


parser = argparse.ArgumentParser(description = 'parse BLAST output and write '
                                               'to tab-delimited file')

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

blastParse = SearchIO.parse(inputFile, 'blast-text')
dbInfo = next(blastParse)
hitInfo = dbInfo[0]
hspInfo = hitInfo[0]

# print(dir(dbInfo))
# print()
# print(dir(hitInfo))
# print()
# print(dir(hspInfo))
# print(float(hspInfo.ident_num)/float(hspInfo.query_span)) # identity
# print(float(hspInfo.query_span)/float(dbInfo.seq_len)) # coverage
# print(hspInfo.pos_num)



FILE_OUT = open(outputFile, 'w')

# write header line
headerL = ['Query_ID', 'Best_hit_ID', 'Identity(%)', 'Coverage(%)']
FILE_OUT.write('\t'.join(headerL) + '\n')

# write data
for qResult in blastParse:
    for hit in qResult:
        for hsp in hit:
            dataL = []
            identHsp = float(hsp.ident_num) / float(hsp.query_span)
            coverHsp = float(hsp.query_span) / float(qResult.seq_len)
            if identHsp > 0.8 and coverHsp > 0.7:

                dataL.append(hsp.query_id) # Query_ID
                dataL.append(hsp.hit_id) # Best_hit_ID
                dataL.append("{0:.2f}".format(identHsp * 100.0)) # Identity percentage
                dataL.append("{0:.2f}".format(coverHsp * 100.0)) # Coverage percentage

                # .join is not method for type int
                FILE_OUT.write('\t'.join(map(str, dataL)) + '\n')

            else:
                break
# print(counter)
FILE_OUT.close()