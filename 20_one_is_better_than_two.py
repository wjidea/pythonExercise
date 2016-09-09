#! /usr/bin/python

# 20_one_is_better_than_two.py

# read fasta file line by line, catch header using regex, and find glycosyl
# from fasta header file. This fasta file should have 50 glycosyl terms in its
# header information. Exclude the 'groups' from the header information, which
# get them down to 15 hits

# change the if statement into one line


# Jie Wang
# September 6, 2016

import sys
import re

faFilePath=sys.argv[1]

FILE=open(faFilePath, 'r')
counter = 0

while True:
    line=FILE.readline()
    if not line:
        break
    # if line.startswith('>'):
        # if re.match(r'.*glycosyl.*', line) and \
        #         not re.match(r'.*groups.*', line):
    if line.startswith('>') and 'glycosyl' in line and 'groups' not in line:
        print(line.rstrip())
        counter += 1
# print('{} seuqneces.'.format(counter))

FILE.close()