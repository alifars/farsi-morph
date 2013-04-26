#!/usr/bin/python
#infer_morph.py
#Weston Feely
#4/25/13
import sys, re

def main(args):
	#Check for required args
	if len(args) < 2:
		print "Usage: python infer_morph.py part-of-speech"
		return 1
	#Read in args
	corpus = open("../data/A.txt").readlines() + open("../data/B.txt").readlines() + open("../data/C.txt").readlines()
	check_pos = args[1].lower()
	#Add all lemmas with specified POS tag to lemmas set, token+lemma pairs to pairs set
	prefixes = set()
	suffixes = set()
	for line in corpus:
		#Strip whitespace off line edges and split on tab
		lis = line.strip().split('\t')
		#Strip token edges of whitespace and ZWNJ
		token = lis[0].strip().decode('utf-8').strip(u'\u200c').encode('utf-8')
		#Substitute ZWNJ for space internally in token
		token = re.sub(' ','\xe2\x80\x8c',token)
		#Strip lemmas edges of whitespace and ZWNJ
		lemma = lis[1].strip().decode('utf-8').strip(u'\u200c').encode('utf-8')
		#Substitute ZWNJ for space internally in lemma
		lemma = re.sub(' ','\xe2\x80\x8c',lemma)
		#Skip lemma == token
		if lemma == token:
			continue
		#Strip pos tag edges of whitespace and lowercase it
		pos = lis[2].strip().lower()
		#If this is the POS we're looking for, add the lemma to our list
		if check_pos == pos:
			if pos != 'v':
				#Check lemma against token
				if re.match(lemma,token):
					#Suffix match
					suffixes.add(token[len(lemma):])
				else:
					#Prefix match
					for i in xrange(0,len(token)):
						if re.match(lemma,token[i:]):
							prefixes.add(token[:i])
			else:
				for l in lemma.split('#'):
					#Check lemma against token
					if re.match(lemma,token):
						#Suffix match
						suffixes.add(token[len(lemma):])
					else:
						#Prefix match
						for i in xrange(0,len(token)):
							if re.match(lemma,token[i:]):
								prefixes.add(token[:i])
	print "Prefixes:"
	for item in prefixes:
		print "+"+check_pos.capitalize()+":"+item+"^"
	print "\nSuffixes:"
	for item in suffixes:
		print "+"+check_pos.capitalize()+":^"+item
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
