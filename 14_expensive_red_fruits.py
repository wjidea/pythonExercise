#! /usr/bin/python

# 14_expensive_red_fruits.py

# Write a script that will read the plu_codes_and_fruit_veggie_names.txt
# plu_codes_and_fruit_veggie_prices.txt, and plu_codes_and_fruit_veggie_prices.
# txt files and write a file that contains the red fruits with their unit price
# more than $0.2.

# Jie Wang
# September 2, 2016

filePricePath = '../plu_codes_and_fruit_veggie_prices.txt'
fileNamePath = '../plu_codes_and_fruit_veggie_names.txt'
fileColorPath = '../plu_codes_and_fruit_veggie_colors.txt'

FILE_1 = open(filePricePath,'r')
FILE_2 = open(fileNamePath, 'r')
FILE_3 = open(fileColorPath, 'r')

nameDict = {}
priceDict = {}
colorDict = {}
pluRedL = []
pluExpensiveL = []

while True:
    line1 = FILE_1.readline()
    line2 = FILE_2.readline()
    line3 = FILE_3.readline()

    if not (line1 and line2 and line3):
        break

    plu1, fruitPrice = line1.rstrip().split('\t')
    plu2, fruitName = line2.rstrip().split('\t')
    plu3, fruitColor = line3.rstrip().split('\t')
    priceDict[plu1] = fruitPrice
    nameDict[plu2] = fruitName

    # take red fruits
    if fruitColor == "red":
        pluRedL.append(plu3)

    # take fruit price more than $0.2
    if float(fruitPrice.strip('$')) > 0.2:
        pluExpensiveL.append(plu1)

    # print(float(fruitPrice.strip('$'))>0.2)

FILE_1.close()
FILE_2.close()
FILE_3.close()

# intersection to make expensive red fruit List
pluRedExpensiveL = set(pluRedL).intersection(pluExpensiveL)


fileRedPath = '../expensive_red_fruits_prices.txt'
FILE_RED = open(fileRedPath, 'w')

for plu in pluRedExpensiveL:
    # print(nameDict[plu], priceDict[plu])
    FILE_RED.write('{0}\t{1}\n'.format(nameDict[plu], priceDict[plu]))

FILE_RED.close()
