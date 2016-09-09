#! /usr/bin/python

# 2_find_red.py

# find the line with red and print it

# Jie Wang
# August 31, 2016

filePath = '../plu_codes_and_fruit_veggie_colors.txt'
FILE = open(filePath, 'r')

matchWord = "red"

for line in FILE.readlines():
    # contentsL = line.rstrip().split("\t")
    # print(contentsL)
    if matchWord in line:
        print(line.rstrip())

FILE.close()