#! /usr/bin/python

# 30_parseBLAST_biopython.py

# blast populus transcript against arabdopsis transcript and extract evalue
# from blast resulsts (plain text) using biopython SearchIO.

# requirements for this script
# Write the output as Tab-delimited file, which includes:
# 1) Name of the blast database qResult.target
# 2) Name of the Query sequence qResult.id
# 3) Length of the Query sequence qResult.seq_len
# 4) name of the best hit sequence hit.
# 5) length of the best hit sequence
# 6) the number of hsps for the best hit
# 7) the score of the alignment with the best hit
# if two or more equally best hits, data from both should be written to the file

# write a list of this title line and join them with tab




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
# hitInfo = dbInfo[1]
# hspInfo = hitInfo[0]

headerL = ['Target_database', 'Query_ID', 'Query_length', 'Best_hit_ID',
           'Best_hit_length', 'Hsp_num', 'Hsp_score']

targetDB = dbInfo.target

FILE_OUT = open(outputFile, 'w')

# write header line
FILE_OUT.write('\t'.join(headerL) + '\n')

# write data
for qResult in blastParse:
    highestScore = qResult[0][0].bitscore
    for hit in qResult:
        for hsp in hit:
            if hsp.bitscore >= highestScore:
                dataL = []
                dataL.append(targetDB) # Target_database
                dataL.append(hsp.query_id) # Query_ID
                dataL.append(qResult.seq_len) # Query_length
                dataL.append(hsp.hit_id) # Best_hit_ID
                dataL.append(hit.seq_len) # Best_hit_length
                dataL.append(len(hit)) # Hsp_num
                dataL.append(hsp.bitscore) # Hsp_score

                # .join is not method for type int
                # FILE_OUT.write('\t'.join(str(x) for x in dataL) + '\n')
                FILE_OUT.write('\t'.join(map(str, dataL)) + '\n')

            else:
                break
# print(counter)
FILE_OUT.close()