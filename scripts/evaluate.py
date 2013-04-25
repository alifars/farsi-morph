#!/usr/bin/python
#evaluate.py
#Weston Feely
#4/25/13
import sys, re

def main(args):
	#Check for required args
	if len(args) < 3:
		print "Usage: python evaluate.py corpus.lemma corpus.results"
		return 1
	#Read in gold standard lemmas
	gold = []
	for lemma in open(args[1]):
		lemma = lemma.strip()
		if '#' in list(lemma):
			gold.append(tuple([x.strip() for x in lemma.split('#')]))
		else:
			gold.append(lemma)
	#Read in lemma hypotheses from lemmatizer
	hyp_raw = open(args[2]).readlines()
	hyp = [] # list of sets, hypotheses for each token
	buff = set() # buffer set for current hypothesis
	for line in hyp_raw:
		if line.isspace():
			#New lemma, append hypotheses for last lemma to hyp list
			hyp.append(buff)
			buff = set() # restart buffer
		else:
			#New hypothesis for current lemma
			line = line.strip() # strip whitespace
			#print "Before "+line
			line = re.sub('\+[\w\?]+','',line) # remove analysis from lemma
			#print "After "+line
			#Append cleaned-up hyp to current buffer
			if (line != '') and (not line.isspace()):
				buff.add(line)
	assert len(gold) == len(hyp)
	#Get an accuracy score for this corpus	
	acc = 0
	i = 0
	for lemma in gold:
		'''
		#Set up print statement for debugging
		lexp = ''
		if type(lemma) is tuple:
			lexp = ' '.join(lemma)
		else:
			lexp = lemma
		rexp = ' '.join(hyp[i])
		print "Lemma: ["+lexp+"] | Hyp: ["+rexp+"]"
		'''		
		#Check if lemma is a tuple (for verb lemma)
		if type(lemma) is tuple:
			#Loop through verb lemmas in lemma tuple
			for verb_lemma in lemma:
				#If any hypothesis lemma is the same as this gold verb lemma
				if verb_lemma in hyp[i]:
					acc += 1 # count this as an accurate hypothesis
					break # don't give credit for multiple accurate verb lemma hypotheses
		else:
			#If any hypothesis lemma is the same as the gold lemma
			if lemma in hyp[i]:
				acc += 1 # count this as an accurate hypothesis
		i+=1 # move to next hypothesis
	acc = float(acc)/i
	#Write accuracy to stdout
	print acc
	return 0

if __name__ == "__main__":
	sys.exit(main(sys.argv))
