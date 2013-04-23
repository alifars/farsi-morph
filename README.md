Farsi-Morph
Weston Feely
4/23/13

Main repository for Farsi morphological analyzer project.

To Do List:
- (Done) Extract corpus of (token,lemma,POS) triples from Farsi treebank
	- (Done) Remove lines with missing lemmas ("_") from corpus
	- (Done) Normalize Farsi text in corpus
	- (Done) Randomly divide lemma triples into three corpora A, B, C
- (Done) Write a script to print all lemmas for a given POS from a given corpus to stdout
	- (Done) Fix script to strip whitespace and ZWNJ from sides of lemmas
- (Done) Set up farsi.foma and lexicon files
	- (Done) Put lemmas from A corpus into lexicon files
	- (Done) Write basic morphology into lexicon for each open-class POS category
	- (In Progress) Modify lexical morphology to allow repeated application of suffixes
- (In Progress) Make an evaluation script, to get lemma accuracy for a given corpus
- Evaluate on A corpus
- Put lemmas from B corpus into lexicon files
- Evaluate on B corpus
- Put lemmas from C corpora into lexicon files
- Evaluate on C corpus
- (In Progress) Update report
	- (In Progress) Explain POS categories, marking open-class and closed-class
	- (In Progress) Explain Farsi text issues with ZWNJ and solutions found
	- (Done) Explain Farsi verb tokenization issue from treebank
	- Make a table of accuracy results from each corpus evaluation
