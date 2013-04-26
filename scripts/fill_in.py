#!/usr/bin/python
#fill_in.py
#Weston Feely
#4/26/13
import sys, re

#Fills in guesses (original tokens) for blank hypotheses from analyzer
def main(args):
	#Check for required args
	if len(args) < 3:
		print "Usage: python fill_in.py corpus.token corpus.results"
		return 1
	#Read in original tokens
	tokens = []
	for token in open(args[1]):
		tokens.append(token)
	#Read in lemma hypotheses from lemmatizer
	hyp_raw = open(args[2]).readlines()
	hyp = [] # list of lists, hypotheses for each token
	buff = [] # buffer list for current hypothesis
	for line in hyp_raw:
		if line.isspace():
			#New lemma, append hypotheses for last lemma to hyp list
			hyp.append(buff)
			buff = [] # restart buffer
		else:
			#New hypothesis for current lemma
			buff.append(line)
	assert len(tokens) == len(hyp)
	#Fill in missing hypotheses
	out = []
	i = 0
	for item in hyp:
		if item == ['+?\n']:
			out.append(tokens[i])
		else:
			out.append(item)
		i+=1
	#Write output list to file
	f = open(args[2]+".fixed",'w')
	for item in out:
		if type(item) is str:
			f.write(item)
		else:
			for next in item:
				f.write(next)
		f.write('\n')
	f.close()
	return 0

if __name__ == "__main__":
	sys.exit(main(sys.argv))
