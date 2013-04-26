Farsi-Morph
Weston Feely
4/26/13

Main repository for Farsi morphological analyzer project.

To Do List:
- (Done) Extract corpus of (token,lemma,POS) triples from Farsi treebank
	- (Done) Remove lines with missing lemmas from corpus
	- (Done) Normalize Farsi text in corpus
	- (Done) Randomly divide lemma triples into three corpora A, B, C
- (Done) Write a script to print all lemmas for a given POS from a given corpus to stdout
- (Done) Set up farsi.foma and lexicon files
- (Done) Add basic morphology to adj, n, v lexica
- (Done) Infer more complex morphology from data, add to adj, n lexica
- (Done) Make an evaluation script, to get lemma precision-recall for a given corpus
- (Done) Put lemmas from A corpus into lexicon files
- (Done) Evaluate on A corpus
- (Done) Put lemmas from B corpus into lexicon files
- (Done) Evaluate on B corpus
- (Done) Put lemmas from C corpora into lexicon files
- (Done) Evaluate on C corpus
- (Done) Update report
