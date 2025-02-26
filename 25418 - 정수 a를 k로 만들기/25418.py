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

run_baekjoon(1, __file__)
##############################################################################
##############################################################################

import sys
from queue import Queue

A, K = map(int, sys.stdin.readline().split(' '))

li_val = [0] *(K+1)

q = Queue()
q.put(A)

while not q.empty():
    num = q.get()

    if li_val[K] != 0:
        break

    new_nums = [num+1, num *2]
    for n in new_nums:
        if n > K:
            continue
        if li_val[n] != 0:
            continue
        
        li_val[n] = li_val[num] +1
        q.put(n)

print(li_val[K])


        
        
        