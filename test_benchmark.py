# -*- coding: utf-8 -*-
"""
Benchmarking script which creates an input of different length dna sequences.
The function full_patt_match takes an input string that is made into the
reverse complement. A variable size sliding window is applied to the input to 
create patterns to compare to the reverse complement. Then all the matches for
the various patterns are printed with the window size and starting location.
"""

import cProfile, re, timeit, random, sys, os
from matplotlib import pyplot as plt

###############################################################################

#Suppresses print output to prevent print spam and lag
class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout
        
        
def full_patt_match(s, window):
    with HiddenPrints():
        
        #reverse complement
        RC = s.translate(s.maketrans('ACTG', 'TGAC'))[::-1]
        
        #make unique expressions for re.compile    
        len_str2 = len(s)        
        patt = [[s[i:i+win] for i in range(len_str2-win+1)] for win in window]
        
        #compile, find matches, and print results
        for size in patt:
            comp = re.compile("|".join(size))
            matches = re.finditer(comp, RC)
            for match in matches:
                mg = match.group()
                print("Starting Index: %d\tWindow Size: %d\tMatching Word: %s" %(match.start(), len(mg), mg))


if __name__ == "__main__":
    runs = 1
    time = []
    win_size = range(4,13)
    
    #time test for multiple input lengths
    for str_base in range(2,5):
        str_len = 10**str_base
        string = ''.join(random.choice('AGCT') for i in range(str_len))        
        time.append(timeit.timeit(lambda: full_patt_match(string, win_size), number = runs))
       
     
    #test for function calls on highest input length
    cProfile.run("full_patt_match(string, win_size)", sort = 'tottime')
    
    #plot loglog graph of time x input length
    run_len = [10**x for x in range(2,2+len(time))]
    plt.plot(run_len, time, 'b')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('String Length')
    plt.ylabel('Time: Seconds')
    
    print("Time values: ", *time)