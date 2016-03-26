# ALife
Python 2.7

The (very raw) beginnings of an artificial life experiment starting with a framework to convert a genome string into functional code.


genomeGenerator reads genomeAST.txt and prints a genome string and a codon to code string for a model organism.
reproductionFile uses a genome and translation table (created by genomeGenerator) to create a new Python file in the same directory.
genomeAST currently reproduces reproductionFile's code.


Organisms beyond the original are named xxx_yyyyyyyy, where x is a random number, and y is a random alphanumeric. 
The first three are used to indicate location in an alphabetically-sorted directory, and the last eight are maintained as a unique organism name.