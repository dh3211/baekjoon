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
n_li = list(map(int, sys.stdin.readline().split(' ')))
m = int(sys.stdin.readline())
m_li = list(map(int, sys.stdin.readline().split(' ')))

ans = []
n_set = set(n_li)
for i in m_li:
    if i in n_set:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)

