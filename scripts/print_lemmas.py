#!/usr/bin/python
#print_lemmas.py
#Weston Feely
#4/23/13
import sys, re

def main(args):
	#Check for required args
	if len(args) < 3:
		print 'Usage: python print_lemmas.py data/corpus part-of-speech >> src/lexica/part-of-speech.lexc'
		return 1
	#Read in args
	corpus = open(args[1]).readlines()
	check_pos = args[2].lower()
	#Add all lemmas with specified POS tag to lemmas set, token+lemma pairs to pairs set
	lemmas = set()
	pairs = set()
	for line in corpus:
		#Strip whitespace off line edges and split on tab
		lis = line.strip().split('\t')
		#Strip token edges of whitespace and ZWNJ
		token = lis[0].strip().decode('utf-8').strip(u'\u200c').encode('utf-8')
		#Substitute ZWNJ for space internally in token
		token = re.sub(' ','\xe2\x80\x8c',token)
		#Substitute "~" for ZWNJ internally in token	
		#token = re.sub('\xe2\x80\x8c','~',token)
		#Strip lemmas edges of whitespace and ZWNJ
		lemma = lis[1].strip().decode('utf-8').strip(u'\u200c').encode('utf-8')
		#Substitute ZWNJ for space internally in lemma
		lemma = re.sub(' ','\xe2\x80\x8c',lemma)
		#Strip pos tag edges of whitespace and lowercase it
		pos = lis[2].strip().lower()
		#If this is the POS we're looking for, add the lemma to our list
		if check_pos == pos:
			if pos != 'v':
				lemmas.add(lemma)
			else:
				#For verb lemmas, add every verb stem to lemma set 
				for l in lemma.split('#'):
					lemmas.add(l)
			if token != lemma:
				pairs.add((token,lemma))
	#Write pairs to stdout
	#for pair in pairs:
	#	print pair[0]+'\t'+pair[1]
	#Write lemmas to stdout
	for lemma in lemmas:
		#Print "Lemma (tab) PosInf;"
		print lemma+'\t'+check_pos.capitalize()+'Inf;'
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
