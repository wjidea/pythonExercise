#! /usr/bin/python

# 6_PLU_names_regex.py

# parse the fruit and vegies file using regex, and print plu and
# fruit/veggie names

# Jie Wang
# September 1, 2016

import re

filePath = '/Users/wangj/scripts/pyExercise/fruits_veggies.txt'
FILE = open(filePath, 'r')

pattern = re.compile(r'^(\w+)\t(\w+)\t(.+)\t(\d{4})')

# re for the old fruits and veggies file
# pattern = re.compile(r'^(\d{4})\t(.+)\t(\w+)\t(\w+)')

for line in FILE.readlines():
    contentStr = line.rstrip()
    match = pattern.match(contentStr)
    print('{0}\t{1}'.format(match.group(4), match.group(1)))

FILE.close()