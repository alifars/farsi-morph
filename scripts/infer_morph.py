#!/usr/bin/python
#infer_morph.py
#Weston Feely
#4/26/13
import sys, re

def main(args):
	#Check for required args
	if len(args) < 2:
		print "Usage: python infer_morph.py part-of-speech"
		return 1
	#Read in args
	corpus = open("../data/A.txt").readlines() + open("../data/B.txt").readlines() + open("../data/C.txt").readlines()
	check_pos = args[1].lower()
	#Set of affixes
	affixes = set()
	for line in corpus:
		#Strip whitespace off line edges and split on tab
		lis = line.strip().split('\t')
		#Strip token edges of whitespace and ZWNJ
                token = lis[1].strip().decode('utf-8').strip(u'\u200c').encode('utf-8')
                #Substitute ZWNJ for space or #-character internally in token
		token = re.sub(' ','\xe2\x80\x8c',token)
		token = re.sub('\#','\xe2\x80\x8c',token)
                if '#' in list(token):
                    print token;
                #Strip lemmas edges of whitespace and ZWNJ
		lemma = lis[2].strip().decode('utf-8').strip(u'\u200c').encode('utf-8')
		#Substitute ZWNJ for space internally in lemma
		lemma = re.sub(' ','\xe2\x80\x8c',lemma)
		#Skip lemma == token
		if lemma == token:
			continue
		#Strip pos tag edges of whitespace and lowercase it
		pos = lis[3].strip().lower()
		if check_pos == pos:
			if pos == 'v' and '#' in list(lemma):
				for stem in lemma.split('#'):
					#Strip verb stem edges of whitespace and ZWNJ
					stem = stem.strip().decode('utf-8').strip(u'\u200c').encode('utf-8')
					#Substitute ZWNJ for space internally in stem
					stem = re.sub(' ','\xe2\x80\x8c',stem)
					dummy = token.replace(stem,'_')
					if '_' in list(dummy):
						affixes.add(dummy)
			else:
				#Check lemma against token
				dummy = token.replace(lemma,"_")
				if "_" in list(dummy):
					affixes.add(dummy)
	prefixes = set()
	suffixes = set()
	other = set()
	for item in affixes:
		if len(item.split('_')) > 2:
			other.add(item)
			continue
		prefix = item.split('_')[0]
		prefix = prefix.strip().decode('utf-8').strip(u'\u200c').encode('utf-8')
		if (not prefix.isspace()) and (prefix != ''):
			prefixes.add(prefix)
		suffix = item.split('_')[-1]
		suffix = suffix.strip().decode('utf-8').strip(u'\u200c').encode('utf-8')
		if (not suffix.isspace()) and (suffix != ''):
			suffixes.add(suffix)
	print "Prefixes:"
	for item in prefixes:
		print "+"+check_pos.capitalize()+":"+item+"^ "+check_pos.capitalize()+";"
	print "\nSuffixes:"
	for item in suffixes:
		print "+"+check_pos.capitalize()+":^"+item+" #;"
	print "\nOther:"
	for item in other:
		print item
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
