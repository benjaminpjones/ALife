# ALife
Python 2.7

The (very raw) beginnings of an artificial life experiment starting with a framework to convert a genome string into functional code.


genomeGenerator reads genomeAST.txt and prints a genome string and a codon to code string for a model organism.
reproductionFile uses a genome and translation table (created by genomeGenerator) to create a new Python file in the same directory named 000_aaaaaaaa.py.


Organisms are named xxx_yyyyyyyy, where x is a random number, and y is a random alphanumeric. 
The first three characters are used to indicate location in an alphabetically-sorted directory, and the last eight are maintained as a unique organism name.

When the organism files are run, the organisms reproduce, copying their own genome into a new file, and attempt to travel in the directory by renaming themselves.
The probability that an organism moves is based on its metabolism, a decimal between 0 and 1.  An organism with a metabolism .6 has a 60% chance of moving.
If an organism has enough energy to move, the distance it moves is between 1 and 100 times its metabolism.  

