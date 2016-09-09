#! /usr/bin/python

# 16_argparse_with_parameters.py

# Write a script that will read the plu_codes_and_fruit_veggie_names.txt
# plu_codes_and_fruit_veggie_prices.txt, and plu_codes_and_fruit_veggie_prices.
# txt files and write a file that contains the red fruits with their unit price
# more than $0.2. On top of the description, input file or filter parameters
# has to be inputed as argument in cmd line. Include color and prices as
# parameters, which can be modified when you call them on cmd line

# I accidentally completed this function in exercise_15, therefore 15 and 16 are
# identical.

# except I fixed the coding style for the save to dict part

# Jie Wang
# September 6, 2016

import argparse
import os.path
import sys


parser = argparse.ArgumentParser(description = 'This program will read plu code'
                                             ' fruit name, price, and colors. '
                                             'Write a text file with to include'
                                             'possible filtering parameters')

parser.add_argument('-p', '--prices', help = 'input plu prices file',
                    required = True)
parser.add_argument('-c', '--colors', help = 'input plu colors file',
                    required = True)
parser.add_argument('-n', '--names', help = 'input plu names file',
                    required = True)
parser.add_argument('-o', '--output', help = 'output file',
                    required = True)
parser.add_argument('-fc', '--filterColor', help = 'color filter [red]',
                    type = str, default = 'red')
parser.add_argument('-fp', '--filterPrice', help = 'price filter [0.2]',
                    type = float, default = 0.2)
parser.add_argument('-v', '--verbose', help = 'increase verbosity',
                    action = 'store_true')
args = parser.parse_args()

# check if the input fild existed
priceFile = args.prices
colorFile = args.colors
nameFile = args.names
outputFile = args.output
color2Find = str(args.filterColor)
priceFilter = float(args.filterPrice)

filesL = [priceFile, colorFile, nameFile]


if args.verbose:
    # check file path one at a time and tell which one is missing
    for inputFile in filesL:
        if not os.path.isfile(inputFile):
            print('Input file {} does not exist!'.format(inputFile))
            sys.exit()
else:
    # check file path in a bulk, but may not be the optimum case
    if not all(map(os.path.isfile, filesL)):
        print('Missing input file(s)!')
        sys.exit()


# check if output file is present
if os.path.isfile(outputFile):
    print('output file {0} already exists'.format(outputFile))
    sys.exit()

# claim list and dict names
priceDict = {}
pluExpensiveL = []

# open price file
FILE_1 = open(priceFile,'r')
while True:
    line1 = FILE_1.readline()

    if not line1:
        break

    pricePluL = line1.rstrip().split('\t')
    plu1 = pricePluL[0]
    fruitPrice = pricePluL[1]
    priceDict[plu1] = fruitPrice

    # take fruit price more than $0.2
    if float(fruitPrice.strip('$')) > priceFilter:
        pluExpensiveL.append(plu1)
FILE_1.close()

# claim dict
nameDict = {}
# opoen name file
FILE_2 = open(nameFile, 'r')
while True:
    line2 = FILE_2.readline()

    if not line2:
        break

    plu2, fruitName = line2.rstrip().split('\t')
    nameDict[plu2] = fruitName
FILE_2.close()

# claim dict and list
colorDict = {}
pluRedL = []

# open color file
FILE_3 = open(colorFile, 'r')
while True:
    line3 = FILE_3.readline()

    if not line3:
        break

    plu3, fruitColor = line3.rstrip().split('\t')
    # take red fruits
    if fruitColor == color2Find:
        pluRedL.append(plu3)

FILE_3.close()

# intersection to make expensive red fruit List
pluRedExpensiveL = set(pluRedL).intersection(pluExpensiveL)

# write the file
fileRedPath = outputFile
FILE_RED = open(fileRedPath, 'w')

for plu in pluRedExpensiveL:
    # print(nameDict[plu], priceDict[plu])
    FILE_RED.write('{0}\t{1}\n'.format(nameDict[plu], priceDict[plu]))

FILE_RED.close()
