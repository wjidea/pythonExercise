#! /usr/bin/python

# 17_print_fa_headers.py

# read fasta file line by line, catch header using regex, and print them
# to terminal

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
    if re.search(r'^>{1}', line):
        print(line.rstrip())
        # counter += 1
# print(counter)

FILE.close()

