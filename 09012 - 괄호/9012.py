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

def check(li):
    c = 0
    while li:
        if li.pop() == ')':
            c+=1
        else:
            c-=1
        
        if c<0:
            return print('NO')
    
    if c == 0:
        print('YES')
    else:
        print('NO')

n = int(sys.stdin.readline())

for _ in range(n):
    s = list(sys.stdin.readline().strip())
    check(s)
