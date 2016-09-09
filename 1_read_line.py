#! /usr/bin/python

# 1_read_line.py

# read lines and print to terminal

# Jie Wang
# August 31, 2016

filePath = '../plu_codes_and_fruit_veggie_names.txt'
FILE = open(filePath, 'r')

for line in FILE.readlines():
    print(line)

FILE.close()