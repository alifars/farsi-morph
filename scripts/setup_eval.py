#!/usr/bin/python
#setup_eval.py
#Weston Feely
#4/26/13
import sys, re

#Extracts the tokens and lemmas from a given corpus text file, separates them into token and lemma lists, ready for evaluation
def main(args):
	if len(args) < 2:
		print "Usage: python setup_eval.py corpus.txt"
		return 1
	#Read in corpus from file
	corpus = open(args[1]).readlines()
	tokens = []
	lemmas = []
	#Loop through lines in corpus
	for line in corpus:
		#Strip whitespace off line edges and split on tab
		lis = line.strip().split('\t')
		#Strip token edges of whitespace and ZWNJ
		token = lis[0].strip().decode('utf-8').strip(u'\u200c').encode('utf-8')
		#Substitute ZWNJ for space or #-character internally in token
		token = re.sub(' ','\xe2\x80\x8c',token)
		token = re.sub('\#','\xe2\x80\x8c',token)
		#Strip lemmas edges of whitespace and ZWNJ
		lemma = lis[1].strip().decode('utf-8').strip(u'\u200c').encode('utf-8')
		#Substitute ZWNJ for space internally in lemma
		lemma = re.sub(' ','\xe2\x80\x8c',lemma)
		#Don't use empty lemmas
		if lemma.isspace() or lemma == '' or lemma.decode('utf-8') == u'\u200c':
			continue
		#Append token to tokens list
		tokens.append(token)
		#Appen lemma to lemmas list
		lemmas.append(lemma)
	assert len(tokens) == len(lemmas)
	#Write tokens to file
	f = open(args[1][:-4]+'.token','w')
	for token in tokens:
		f.write(token+'\n')
	f.close()
	#Write lemmas to file
	f = open(args[1][:-4]+'.lemma','w')
	for lemma in lemmas:
		f.write(lemma+'\n')
	f.close()
	return 0

if __name__ == "__main__":
	sys.exit(main(sys.argv))
