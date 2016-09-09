#! /usr/bin/python

# 7_plu_names_split.py

# parse the fruit and vegies file using the split function, and print plu and
# names

# Jie Wang
# September 1, 2016

filePath = '/Users/wangj/scripts/pyExercise/fruits_veggies.txt'
FILE = open(filePath, 'r')

for line in FILE.readlines():
    lineT = line.rstrip().split('\t')
    plu = lineT[3]
    fruit = lineT[0]
    print('{0}\t{1}'.format(plu, fruit))
    # print(lineT)

