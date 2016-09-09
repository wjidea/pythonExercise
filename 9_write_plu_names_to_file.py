#! /usr/bin/python

# 9_write_plu_names_to_file.py

# parse the fruit and vegies file using the split function, and store them
# in a dictionary

# Jie Wang
# September 1, 2016

# Read the file and parse them into Dict
filePath = '../fruits_veggies.txt'
FILE_1 = open(filePath, 'r')

marketDict = {}

for line in FILE_1.readlines():
    lineT = line.rstrip().split()
    plu, fruit = lineT[3], lineT[0]
    marketDict[plu] = fruit
    # print('{0}\t{1}'.format(plu, fruit))

FILE_1.close()


# write dict into a text file
newFilePath = '../plu_codes_and_fruit_veggie_names.txt'
FILE_2 = open(newFilePath, 'w')

for key in marketDict.keys():
    FILE_2.write('{0}\t{1}\n'.format(key, marketDict[key]))

FILE_2.close()