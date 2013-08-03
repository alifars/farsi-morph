#!/usr/bin/python
#random_split_3sets.py
#Weston Feely
#4/24/13
import sys, re, random

'''Splits Farsi tokens data file into three sets (A B C), randomly choosing a user defined percentage of the sentences as the A and B sets and placing the remainder of the sentences into the C set.
Writes three files to the current directory: A.txt, B.txt and C.txt'''
def main(args):
	#Check args
	if len(args) < 4:
		print "Usage: python random_split_3sets.py farsi_tokens.txt A_fraction B_fraction"
		return 1
	#Read Farsi tokens data from file
	filename = args[1]
	data = open(filename).readlines()
	#Get data split percentages
	A_fraction = float(args[2])
	B_fraction = float(args[3])
	#Exception for decimal out of range
	if (A_fraction <= 0.0) or (A_fraction >= 1.0) or (B_fraction <= 0.0) or (B_fraction >= 1.0) or (A_fraction+B_fraction >= 1.0):
		print 'Error! A_fraction and B_fraction must be between 0 and 1.0'
		print 'Usage: python random_split_3sets.py farsitokens.txt A_fraction B_fraction'
		return 1
	#Shuffle data
	random.shuffle(data)
	#Split shuffled data into three sets
	num_A = int(len(data)*A_fraction) # number of tokens to be in A data set
	num_B = int(len(data)*B_fraction) # number of tokens to be in B data set
	A_lis = [] # list of strings, to write to file as A data set
	B_lis = [] # list of strings, to write to file as B data set
	C_lis = [] # list of string, to write to file as C data set
	#Loop through data
	for i in range(0,len(data)):
            #kensuke-mi add code below to use in my environment
            if data[i]=='\n' or data[i]=='\r\n':
                pass;
            else:
		if i < num_A:
			#Put token in A list
                        A_lis.append(data[i])
		elif i < (num_A+num_B):
			#Put token in B list
			B_lis.append(data[i])
		else:
			#Put token in C list
                        C_lis.append(data[i])
        #Sort token lists by POS tag
        A_lis.sort(key=lambda s: s.split('\t')[2].strip())
	B_lis.sort(key=lambda s: s.split('\t')[2].strip())
	C_lis.sort(key=lambda s: s.split('\t')[2].strip())

        #Write sets to file
	A_file_name = 'A.txt'
	B_file_name = 'B.txt'
	C_file_name = 'C.txt'
	#Write A set
	f = open(A_file_name,'w')
	for line in A_lis:
		f.write(line)
	f.close()
	#Write B set
	f = open(B_file_name,'w')
	for line in B_lis:
		f.write(line)
	f.close()
	#Write C set
	f = open(C_file_name,'w')
	for line in C_lis:
		f.write(line)
	f.close()
	#Tell user it was sucessful, give number of sentences
	print 'Success! A set written to '+A_file_name+', B set written to '+B_file_name+', C set written to '+C_file_name
	print '#Tokens in original file: '+str(len(data))
	print '#Tokens in A set: '+str(num_A)
	print '#Tokens in B set: '+str(num_B)
	print '#Tokens in C set: '+str(len(data)-(num_A+num_B))
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
