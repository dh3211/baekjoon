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
"""
10 1
12 2
23 3
21 4
32 5
34 6
43 7
45 8
54 9
56 10
65 11
67 12
76 13
78 14
87 15
89 16
98 17

"""
import sys

n = int(sys.stdin.readline())
li = [0, 9]
lili = [
    [0]*10,
    [0] + [1]*9
    ]

for idx in range(2, n+1):
    ex = lili[idx-1]
    tmp = [0] *10
    tmp[0] = ex[1]
    for i in range(1,9):
        tmp[i] = ex[i-1] +ex[i+1]
        tmp[i] = tmp[i]%1000000000
    tmp[9] = ex[8]

    lili.append(tmp)

print(sum(lili[-1])%1000000000)


