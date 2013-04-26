#!/usr/bin/python
#evaluate.py
#Weston Feely
#4/26/13
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
	#Compute precision-recall for the analysis of this corpus
	correct = 0 # number of correct matches
	num_gold = 0 # total number of gold standard lemmas
	num_hyp = 0 # total number of produced analyses
	i = 0 # hypothesis counter
	for lemma in gold:
		#Check if lemma is a tuple (for verb lemma)
		if type(lemma) is tuple:
			num_gold += len(lemma)
			#Loop through verb lemmas in lemma tuple
			for verb_lemma in lemma:
				#If any hypothesis lemma is the same as this gold verb lemma
				if verb_lemma in hyp[i]:
					correct += 1 # count this as an accurate hypothesis
		else:
			num_gold += 1
			#If any hypothesis lemma is the same as the gold lemma			
			if lemma in hyp[i]:
				correct += 1 # count this as an accurate hypothesis
		num_hyp += len(hyp[i])		
		i+=1 # move to next hypothesis
	#Write accuracy to stdout
	letter = args[1].split('/')[-1][0]
	p = float(correct)/num_hyp
	r = float(correct)/num_gold
	print "Corpus "+letter
	print "Precision="+str(p)
	print str(correct)+" correct lemmas out of "+str(num_hyp)+" total analysis hypotheses"
	print "Recall="+str(r)
	print str(correct)+" correct lemmas out of "+str(num_gold)+" total lemmas"
	print "F-Score="+str(2*((p*r)/(p+r)))
	return 0

if __name__ == "__main__":
	sys.exit(main(sys.argv))
