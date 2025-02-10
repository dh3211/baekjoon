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

T = int(sys.stdin.readline())
n_li = []
for _ in range(T):
    n = int(sys.stdin.readline())
    n_li.append(n)

li = [1,1,2,4]
for idx in range(4, max(n_li)+1):
    val = li[idx-1] +li[idx-2] +li[idx-3]
    li.append(val)

for idx in n_li:
    print(li[idx])
