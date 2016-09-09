#! /usr/bin/python

# 11_write_plu_color.py

# parse the fruit and vegies file using the split function,and store them
# in a dictionary. Key is the PLU code, and price and names will be in a list

# Jie Wang
# September 1, 2016

# Read the file and parse them into Dict
filePath = '../fruits_veggies.txt'
FILE_1 = open(filePath, 'r')

marketDict = {}

for line in FILE_1.readlines():
    lineT = line.rstrip().split()
    fruit, color, price, plu = lineT
    marketDict[plu] = [fruit, price, color]
    # print('{0}\t{1}'.format(plu, color))

FILE_1.close()


# write dict into a text file
newFilePath = '../plu_codes_and_fruit_veggie_colors.txt'
FILE_2 = open(newFilePath, 'w')

for key in marketDict.keys():
    FILE_2.write('{0}\t{1}\n'.format(key, marketDict[key][2]))

FILE_2.close()