#! /usr/bin/python

# 3_parse_fruit_regex.py

# match the word and print the line

# Jie Wang
# August 31, 2016

import re

filePath = '../plu_codes_and_fruit_veggie_names.txt'
FILE = open(filePath, 'r')

pattern = re.compile('(\d+)\t(\w+)')

for line in FILE.readlines():
    contentsStr = line.rstrip()
    # print(contentsStr)
    match = pattern.match(contentsStr)
    print(match.group(2))

FILE.close()