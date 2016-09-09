#! /usr/bin/python

# 19_glycosyl_no_groups.py

# read fasta file line by line, catch header using regex, and find glycosyl
# from fasta header file. This fasta file should have 50 glycosyl terms in its
# header information. Exclude the 'groups' from the header information, which
# get them down to 15 hits


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
    # if re.match(r'^>{1}.*glycosyl.*', line):
    #     if not re.match(r'.*groups.*', line):
    if 'glycosyl' in line:
        if 'groups' not in line:
            print(line.rstrip())
            counter += 1
print(counter)

FILE.close()