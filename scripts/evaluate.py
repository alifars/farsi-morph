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
	gold = [x.strip() for x in open(args[1]).readlines()]
	#Read in lemma hypotheses from lemmatizer
	hyp_raw = open(args[2]).readlines()
	hyp = [] # list of lists, hypotheses for each token
	buff = []
	for line in hyp_raw:
		if line.isspace():
			#New lemma, append hypotheses for last lemma to hyp list
			hyp.append(buff)
		else:
			#New hypothesis for current lemma
			line = line.strip() # strip whitespace
			#print "Before "+line
			line = re.sub('\+[\w\?]+','',line) # remove analysis from lemma
			#print "After "+line
			#Append cleaned-up hyp to current buffer
			if (line != '') and (not line.isspace()):
				buff.append(line)
	assert len(gold) == len(hyp)
	#Get an accuracy score for this corpus	
	acc = 0
	i = 0
	for lemma in gold:
		if lemma in hyp[i]:
			acc += 1
		i+=1
	acc = float(acc)/i
	#Write accuracy to stdout
	print acc
	return 0

if __name__ == "__main__":
	sys.exit(main(sys.argv))
