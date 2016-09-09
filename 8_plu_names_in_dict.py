#! /usr/bin/python

# 8_plu_names_in_dict.py

# parse the fruit and vegies file using the split function, and store them
# in a dictionary

# Jie Wang
# September 1, 2016

filePath = '/Users/wangj/scripts/pyExercise/fruits_veggies.txt'
FILE = open(filePath, 'r')

marketDict = {}

for line in FILE.readlines():
    lineT = line.rstrip().split()
    plu = lineT[3]
    fruit = lineT[0]
    marketDict[plu] = fruit
    # print('{0}\t{1}'.format(plu, fruit))

FILE.close()

for plu in marketDict:
    print('{0}\t{1}'.format(plu, marketDict[plu]))