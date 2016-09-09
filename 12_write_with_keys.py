#! /usr/bin/python

# 12_write_with_keys.py

# Write a script that will read the plu_codes_and_fruit_veggie_names.txt and
# plu_codes_and_fruit_veggie_prices.txt files and write a file that contains
# the fruit/veggie names and prices without PLU codes.

# Jie Wang
# September 2, 2016

filePricePath = '../plu_codes_and_fruit_veggie_prices.txt'
fileNamePath = '../plu_codes_and_fruit_veggie_names.txt'

FILE_1 = open(filePricePath,'r')
FILE_2 = open(fileNamePath, 'r' )

nameDict = {}
priceDict = {}

while True:
    line1 = FILE_1.readline()
    line2 = FILE_2.readline()
    if not (line1 and line2):
        break
    plu1, fruitPrice = line1.rstrip().split('\t')
    plu2, fruitName = line2.rstrip().split('\t')
    priceDict[plu1] = fruitPrice
    nameDict[plu2] = fruitName

FILE_1.close()
FILE_2.close()

FILE_3 = open('../fruit_veggie_names_and_fruit_veggie_prices.txt', 'w')
for key in nameDict.keys():
    FILE_3.write('{0}\t{1}\n'.format(nameDict[key], priceDict[key]))
    # print('{0}\t{1}'.format(nameDict[key], priceDict[key]))
FILE_3.close()