# ALife
Python 2.7

The (very raw) beginnings of an artificial life experiment starting with a framework to convert a genome string into functional code.


genomeGenerator reads genomeAST.txt and prints a genome string and a codon to code string for a model organism.
reproductionFile uses a genome and translation table (created by genomeGenerator) to create a new Python file in the same directory.
genomeAST currently reproduces reproductionFile's code.
