#!/usr/bin/python
#print_lemmas.py
#Weston Feely
#4/25/13
import sys, re

def main(args):
	#Check for required args
	if len(args) < 3:
		print "Usage: python print_lemmas.py corpus.txt part-of-speech >> part-of-speech.lexc"
		return 1
	#Read in args
	corpus = open(args[1]).readlines()
	check_pos = args[2].lower()
	#Add all lemmas with specified POS tag to lemmas set
	lemmas = set()
	for line in corpus:
                #Strip whitespace off line edges and split on tab
		lis = line.strip().split('\t')
		#Strip token edges of whitespace and ZWNJ
		token = lis[1].strip().decode('utf-8').strip(u'\u200c').encode('utf-8')
		#Substitute ZWNJ for space or #-character internally in token
		token = re.sub(' ','\xe2\x80\x8c',token)
		token = re.sub('\#','\xe2\x80\x8c',token)
		#Strip lemmas edges of whitespace and ZWNJ
		lemma = lis[2].strip().decode('utf-8').strip(u'\u200c').encode('utf-8')
		#Substitute ZWNJ for space internally in lemma
		lemma = re.sub(' ','\xe2\x80\x8c',lemma)
		#Don't use empty lemmas
		if lemma.isspace() or lemma == '':
			continue
		#Strip pos tag edges of whitespace and lowercase it
		pos = lis[3].strip().lower()
		#If this is the POS we're looking for, add the lemma to our list
		if check_pos == pos:
			#Check if POS is verb
			if pos != 'v':
				#Add lemma to lemmas set
				lemmas.add(lemma)
			else:
				#Check for #-character in verb lemma
				if '#' in list(lemma):
					#Add every verb stem to lemma set 
					for stem in lemma.split('#'):
						#Strip verb stem edges of whitespace and ZWNJ
						stem = stem.strip().decode('utf-8').strip(u'\u200c').encode('utf-8')
						#Substitute ZWNJ for space internally in stem
						stem = re.sub(' ','\xe2\x80\x8c',stem)
						#Add stem to lemmas set
						lemmas.add(stem)
				else:
					lemmas.add(lemma)
	#Write lemmas to stdout
	for lemma in lemmas:
		#Print "Lemma (tab) PosInf;"
		print lemma+'\t'+check_pos.capitalize()+'Inf;'
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
