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

n = int(sys.stdin.readline())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split(' '))
    a_li = [a]
    b_li = [b]
    while a != 1:
        a = a//2
        a_li.append(a)
    while b != 1:
        b = b//2
        b_li.append(b)
    
    for ele in a_li:
        if ele in b_li:
            print(ele *10)
            break
