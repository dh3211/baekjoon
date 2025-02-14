import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from __baekjoon__.run import run_baekjoon

'''
int(sys.stdin.readline())
sys.stdin.readline().strip()
map(int, sys.stdin.readline().split(' '))
list(map(int, sys.stdin.readline().split(' ')))
'''

run_baekjoon(3, __file__)
##############################################################################
##############################################################################

import sys
input_ = sys.stdin.readline().strip()
try:
    n_input, st_input = input_.split(' ')

    exist_st_input = 1
except:
    n_input = input_
    exist_st_input = 0

n_input = int(n_input)
max_n = 2**(n_input +1) -1

if not exist_st_input:
    print(max_n)

else:
    i, j = 0, 0
    val = max_n
    f = max_n
    for st in st_input:
        f -= 2**(i) 
        i += 1
        j *= 2
        if st == 'R':
            j += 1
        
        val = f-j
    
    print(val)