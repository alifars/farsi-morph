#!/usr/bin/python
# -*- coding: utf-8 -*- 
#norm_farsi.py
#Weston Feely
#4/25/13
import sys, re

#Normalizes Farsi text, removing diacritics (except alef madde) and converting Arabic ya to Farsi ye
def main(args):
	#Check for required args
	if len(args) < 2:
		print "Usage: python norm_farsi.py input_filename"
		return 1
	#Read in text
	infile = args[1]
	intext = open(infile).readlines()
	#Diacritics
	diacritics = set([u'\u0610',u'\u0611',u'\u0612',u'\u0613',u'\u0614',u'\u0615',u'\u0616',u'\u0617',u'\u0618',u'\u0619',
			u'\u061a',u'\u064b',u'\u064c',u'\u064d',u'\u064e',u'\u064f',u'\u0650',u'\u0651',u'\u0652',u'\u0653',
			u'\u0654',u'\u0655',u'\u0656',u'\u0657',u'\u0658',u'\u0659',u'\u065a',u'\u065b',u'\u065c',u'\u065d',
			u'\u065e',u'\u065f',u'\u0670',u'\u06d6',u'\u06d7',u'\u06d8',u'\u06d9',u'\u06da',u'\u06db',u'\u06dc',
			u'\u06df',u'\u06e0',u'\u06e1',u'\u06e2',u'\u06e3',u'\u06e4',u'\u06e7',u'\u06e8',u'\u06ea',u'\u06eb',
			u'\u06ec',u'\u06ed'])
	#Loop through input text
	outtext = []
	for line in intext:
		#Normalize text
		line = line.strip()
		#Remove all diacritics
		for item in diacritics:
			line = re.sub(item,u'',line.decode('utf-8')).encode('utf-8')
		#Normalize alef (except alef madde)
		line = re.sub('أ','ا',line)
		line = re.sub('إ','ا',line)
		#line = re.sub('آ','ا',line)
		#Normalize heh
		line = re.sub('ۀ','ه',line)
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
