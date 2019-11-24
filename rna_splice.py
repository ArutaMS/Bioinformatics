# -*- coding: utf-8 -*-
"""
Takes as input a fasta file with a sequence followed by introns and prints the
resulting protein.
"""

import sys
from functools import reduce

rna2AA = {'UUU':'F', 'UUC': 'F', 'UUA':'L', 'UUG':'L', 'UCU': 'S', 'UCC': 'S'\
           ,'UCA': 'S', 'UCG':'S', 'UAU':'Y', 'UAC':'Y', 'UGU':'C', 'UGC':'C'\
           ,'UGG': 'W','CUU':'L', 'CUC':'L','CUA':'L','CUG':'L','CCU':'P',\
           'CCC':'P','CCA':'P','CCG':'P','CAU':'H','CAC':'H','CAA':'Q','CAG':\
           'Q','CGU':'R','CGC':'R','CGA':'R','CGG':'R','AUU':'I','AUC':'I'\
           ,'AUA':'I','AUG':'M','ACU':'T','ACC':'T','ACA':'T','ACG':'T',\
           'AAU':'N','AAC':'N','AAA':'K','AAG':'K','AGU':'S','AGC':'S',\
           'AGA':'R','AGG':'R','GUU':'V','GUC':'V','GUA':'V','GUG':'V',\
           'GCU':'A','GCC':'A','GCA':'A','GCG':'A','GAU':'D','GAC':'D',\
           'GAA':'E','GAG':'E','GGU':'G','GGC':'G','GGA':'G','GGG':'G',\
           'UAA':'Stop','UAG':'Stop','UGA':'Stop'}

#read file
with open(sys.argv[1], 'r') as file:
    fasta = file.read().split('\n')

#seperate file into sequence and introns
for ii in range(len(fasta)):
    if ii > 0 and fasta[ii][0] == '>':
        seq = ''.join(fasta[1:ii])
        fasta = fasta[ii:]
        break

#remove introns then convert to RNA
seq= reduce(lambda x,i: x.replace(i,''), fasta[1::2], seq)    
seq = seq.replace('T', 'U')

#seperate into groups of 3
trans = list(zip(*([iter(''.join(seq))]*3)))

#convert amino acids into protein
prot = []
for AA in trans:
    if rna2AA[''.join(AA)] == 'Stop':
        break
     
    prot.append(rna2AA[''.join(AA)])

     
print(''.join(prot))

