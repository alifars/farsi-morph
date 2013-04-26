#!/bin/bash
#add_lemmas_from_corpus.sh
#Weston Feely
#4/26/13

#Read in corpus letter from args
corpus=$1

#Add lemmas from this corpus to each POS lexicon
./print_lemmas.py ../data/${corpus}.txt adj >> ../src/lexica/adj.lexc
./print_lemmas.py ../data/${corpus}.txt adr >> ../src/lexica/adr.lexc 
./print_lemmas.py ../data/${corpus}.txt adv >> ../src/lexica/adv.lexc
./print_lemmas.py ../data/${corpus}.txt conj >> ../src/lexica/conj.lexc
./print_lemmas.py ../data/${corpus}.txt iden >> ../src/lexica/iden.lexc
./print_lemmas.py ../data/${corpus}.txt n >> ../src/lexica/n.lexc
./print_lemmas.py ../data/${corpus}.txt part >> ../src/lexica/part.lexc
./print_lemmas.py ../data/${corpus}.txt posnum >> ../src/lexica/posnum.lexc
./print_lemmas.py ../data/${corpus}.txt postp >> ../src/lexica/postp.lexc
./print_lemmas.py ../data/${corpus}.txt prem >> ../src/lexica/prem.lexc
./print_lemmas.py ../data/${corpus}.txt prenum >> ../src/lexica/prenum.lexc
./print_lemmas.py ../data/${corpus}.txt prep >> ../src/lexica/prep.lexc
./print_lemmas.py ../data/${corpus}.txt pr >> ../src/lexica/pr.lexc
./print_lemmas.py ../data/${corpus}.txt psus >> ../src/lexica/psus.lexc
./print_lemmas.py ../data/${corpus}.txt punc >> ../src/lexica/punc.lexc
./print_lemmas.py ../data/${corpus}.txt subr >> ../src/lexica/subr.lexc
./print_lemmas.py ../data/${corpus}.txt v >> ../src/lexica/v.lexc

