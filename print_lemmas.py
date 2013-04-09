#!/usr/bin/python
#print_lemmas.py
#Weston Feely
#4/8/13
import sys

def main(args):
	#Check for required args
	if len(args) < 3:
		print 'Usage: python print_lemmas.py corpus part-of-speech >> ../src/lexica/part-of-speech.lexc'
		return 1
	corpus = open(args[1]).readlines()
	check_pos = args[2].lower()
	lemmas = set()
	#Add all lemmas with specified POS tag to lemmas set
	for line in corpus:
		lis = line.split('\t')
		lemma = lis[1]
		pos = lis[2].strip().lower()
		if check_pos == pos:
			lemmas.add(lemma)
	#Write lemmas to stdout
	for lemma in lemmas:
		#Print "Lemma (tab) PosInf;"
		print lemma+'\t'+check_pos.capitalize()+'Inf;'
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
