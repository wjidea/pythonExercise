#! /usr/bin/python

# 5_split_parse.py

# parse the fruit and vegie file using the split function

# Jie Wang
# September 1, 2016

filePath = '/Users/wangj/scripts/pyExercise/fruits_veggies.txt'
FILE = open(filePath, 'r')

for line in FILE.readlines():
    # print(line.rstrip())
    fruit = line.rstrip().split('\t')[0] # print the 2nd col
    print(fruit)