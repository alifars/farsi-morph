#!/bin/bash
#analyze.sh
#Weston Feely
#4/25/13

#Read in corpus letter from args
corpus=$1

#Compile foma file into binary file
cd ../src/
foma -l farsi.foma

#Analyze tokens for this corpus, save into results folder
cat ../data/${corpus}.token | flookup -x farsi.bin > ../results/${corpus}.results
