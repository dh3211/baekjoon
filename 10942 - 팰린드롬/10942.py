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
li = list(map(int, sys.stdin.readline().split(' ')))
li = [0] + li

dp = [[2 for _ in range(n+1)] for _ in range(n+1)]

# S = E
for i in range(1, n+1):
    dp[i][i] = 1

# S = E+1
for i in range(1, n):
    if li[i] == li[i+1]:
        dp[i][i+1] = 1
    else:
        dp[i][i+1] = 0

for length in range(3, n+1):
    for start in range(1, n-length +2):
        s = start
        e = start +length -1

        if li[s] != li[e]:
            dp[s][e] = 0

        elif dp[s+1][e-1] == 0:
            dp[s][e] = 0

        else:
            dp[s][e] = 1

        
# for ll in dp:
#     print(ll)

m = int(sys.stdin.readline())
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split(' '))
    ans = dp[s][e]
    print(ans)
