# -*- coding: utf-8 -*-
"""
Takes an amino acid string as input and calculates the
amount of possible rna codon combinations that could
have produced that string.
"""

import sys

#read file
with open(sys.argv[1], 'r') as file:
    prot_seq = file.read().rstrip()


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

#create dictionary with all possible codons for each amino acid
rnaCount = {}
for key, value in  rna2AA.items(): 
    rnaCount.setdefault(value, set()).add(key)

#convert the dict into amino acids:length of possible codons
rnaCount = {key:len(values) for key, values in rnaCount.items()}

#multiply the possible combinations for each amino acid
tn_trans = 1
for ele in prot_seq:
    tn_trans = tn_trans*rnaCount[ele]

#mod 1m as per project description
print((tn_trans*rnaCount['Stop'])%1000000)
