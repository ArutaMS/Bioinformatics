# -*- coding: utf-8 -*-
"""
Takes two dna sequences in fasta format and prints the transition/transversion
ratio between them. 
"""

import sys

#read file
with open(sys.argv[1], 'r') as file:
    f = file.read().split('>')
    dna = f[1].split('\n',1)[1].replace('\n', '')
    compare = f[2].split('\n',1)[1].replace('\n', '')

#transition pairs   
t = {'A':'G', 'G':'A', 'C':'T', 'T':'C'}

#set transition to 1, transversions to 0 and find ratio    
pair = zip(dna, compare)
x = [1 if t[p1] == p2 else 0 for p1, p2 in pair if p1 != p2]
print(sum(x)/x.count(0))
