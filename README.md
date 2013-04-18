Farsi-Morph
Weston Feely
4/18/13

Main repository for Farsi morphological analyzer project.

To Do List:
- (Done) Extract (token,lemma,POS) triples from Farsi treebank
- (Done) Write a script to randomly divide lemma triples into three corpora A, B, C
- (Done) Write a script to print all lemmas for a given POS from a given corpus to stdout
- (Done) Set up farsi.foma and lexicon files
- (Done) Fix print_lemmas.py to strip whitespace and ZWNJ from sides of lemmas
- (Done) Put lemmas from A corpus into lexicon files
- (Done) Write basic morphology into lexicon for each open-class POS category
- (In Progress) Modify lexical morphology to allow repeated application of suffixes
- Clean up obvious errors in lemmas in corpora (missing lemma '_', clearly erroneous lemmas)
- Make an evaluation script, to get precision-recall for a given corpus.
- Evaluate on A corpus.
- Put lemmas from B corpus into lexicon files
	- Modify print_lemmas.py to overwrite existing lemmas below hand-added entries
	- Print lemmas from A and B corpus, redirect and append to lexicon files
- Evaluate on B corpus.
- Put lemmas from C corpus into lexicon files
- Evaluate on C corpus.
- (In Progress) Update report.
	- (In Progress) Explain POS categories, marking open-class and closed-class
	- (In Progress) Explain Farsi text issues with ZWNJ and solutions found
	- (Done) Explain Farsi verb tokenization issue from treebank
	- Include precision-recall results from each run
