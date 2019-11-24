# -*- coding: utf-8 -*-
"""
Takes a file with line seperated gene IDs and searches
them for the predefined motif. In this case N[-P][ST][-P].
It then prints the ID and the start locations of each motif
or No Locations if the motif is not present.
"""

import sys, re, time, requests

#read file
with open(sys.argv[1], 'r') as file:
    ID_list = file.read().splitlines()

#define motif to search
motif = r'(?=(N[^P][ST][^P]))'
for ID in ID_list:
    #open file and remove leading information
    seq = ''.join(requests.get("http://www.uniprot.org/uniprot/" + ID + '.fasta').text.splitlines()[1:])
    
    #find location of motif
    matches = re.finditer(motif, seq)
    results = [match.start()+1 for match in matches]
        
    #print ID and locations of motif    
    if len(results) > 0:
        print(ID)    
        print(*results)
    else:
        print(ID)
        print('No Locations')

    #don't rapidly access uniprot
    time.sleep(1)