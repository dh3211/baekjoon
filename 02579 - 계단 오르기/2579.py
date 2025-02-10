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
li = [0]
for _ in range(n):
    e = int(sys.stdin.readline())
    li.append(e)

li_li = [[0] for _ in range(3)]

li_li[0].append(li[1]) # OO
li_li[1].append(li[1]) # XO
li_li[2].append(0)     # OX


for i in range(2,n+1):
    li_li[0].append(li_li[1][i-1] +li[i])
    li_li[1].append(li_li[2][i-1] +li[i])
    li_li[2].append(max(li_li[0][i-1], li_li[1][i-1]))

print(max(li_li[0][n], li_li[1][n]))