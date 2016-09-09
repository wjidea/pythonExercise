#! /usr/bin/python

# 18_find_glycosyl.py

# read fasta file line by line, catch header using regex, and find glycosyl
# from fasta header file. This fasta file should have 50 glycosyl terms in its
# header information.


# Jie Wang
# September 3, 2016

import sys
import re

faFilePath=sys.argv[1]

FILE=open(faFilePath, 'r')
counter = 0

while True:
    line=FILE.readline()
    if not line:
        break
    if re.match(r'^>{1}.*glycosyl.*', line):
        print(line.rstrip())
        # counter += 1
# print(counter)

FILE.close()