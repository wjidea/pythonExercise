#! /usr/bin/python

# 4_red_fruit_names.py

# find the red fruit and print them to terminal

# Jie Wang
# August 31, 2016

import re

fileColPath = '../plu_codes_and_fruit_veggie_colors.txt'
fileNamePath = '../plu_codes_and_fruit_veggie_names.txt'

FILECOL = open(fileColPath, 'r')
FILENAME = open(fileNamePath,'r')

pluRedL = []
pattern = re.compile('^(\d+)\t(\w+)')

for line in FILECOL.readlines():
    contentsStr = line.rstrip()
    # print(contentsStr)
    match = pattern.match(contentsStr)
    if match.group(2) == "red":
        pluRedL.append(match.group(1))

for line in FILENAME.readlines():
    contentsStr = line.rstrip()
    # print(contentsStr)
    match = pattern.match(contentsStr)
    if match.group(1) in pluRedL:
        print(match.group(2))

FILECOL.close()
FILENAME.close()