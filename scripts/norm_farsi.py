#!/usr/bin/python
# -*- coding: utf-8 -*- 
#norm_farsi.py
#Weston Feely
#4/21/13
import sys, re

#Normalizes Farsi text, removing diacritics (except alef mada) and converting Arabic ya to Farsi ye
def main(args):
	#Check for required args
	if len(args) < 2:
		print "Usage: python norm_farsi.py input_filename"
		return 1
	#Read in text
	infile = args[1]
	intext = open(infile).readlines()
	#Diacritics
	diacritics = set(['\xd9\x92','\xd9\x91','\xd9\x90','\xd9\x8f','\xd9\x8e','\xd9\x8d','\xd9\x8c','\xd9\x8b'])
	#Loop through input text
	outtext = []
	for line in intext:
		#Normalize text
		line = line.strip()
		#Remove all diacritics (except alef mada)
		for item in diacritics:
			line = re.sub(item,'',line)
		#Normalize alef (except alef mada)
		line = re.sub('أ','ا',line)
		line = re.sub('إ','ا',line)
		#line = re.sub('آ','ا',line)
		#Convert Arabic ya to Farsi ye
		line = re.sub('ي','ﻯ',line)
		#Append to output list
		outtext.append(line)
	#Write normalized text to file
	f = open(infile+".norm",'w')
	for line in outtext:
		f.write(line+'\n')
	f.close()
	return 0

if __name__ == "__main__":
	sys.exit(main(sys.argv))
