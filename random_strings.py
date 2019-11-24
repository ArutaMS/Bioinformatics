# -*- coding: utf-8 -*-
"""
Takes as input a dna sequence followed by number between 0 and 1 representing
possible GC contents of the string. Prints the log10 probability that each GC 
content produced the given string. 
"""

import numpy as np
import sys

#read file and seperate into sequence and GC content
with open(sys.argv[1], 'r') as file:
    file = file.read().split('\n')
    string = file[0]
    content = np.array([float(x) for x in file[1:][0].split()])

#probability of each nucleotide
GC = np.array(content/2)
AT = np.array((1-content)/2)

#probability of sequence
prob = np.array([1] * len(GC))
for nuc in string:
    if nuc == 'A' or nuc == 'T':
        prob = prob*AT
    elif nuc == 'C' or nuc == 'G':
        prob = prob*GC

print(np.log10(prob))
            