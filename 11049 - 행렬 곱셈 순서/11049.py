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

run_baekjoon(2, __file__)
##############################################################################
##############################################################################

import sys

n = int(sys.stdin.readline())
input_li = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split(' '))
    input_li.append([a,b])

dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n-1):
    dp[i][i+1] = input_li[i][0]*input_li[i][1]*input_li[i+1][1]
# print(dp)

for length in range(2,n+1):
    for start in range(n):
        end = start + length
        if end >= n:
            continue

        tmp = []
        # print(start, end)
        for l in range(length):
            crit = start +l

            val = input_li[start][0]*input_li[crit+1][0]*input_li[end][1]
            
            if start !=crit:
                val += dp[start][crit]
            if end != crit +1:
                val += dp[crit+1][end]

            tmp.append(val)

            # print(f'star : {start}, crit : {crit}, end : {end}')
            # print(dp[start][crit], dp[crit+1][end],'\t',\
            #       input_li[start][0], input_li[end][1], input_li[crit+1][1])
            # print(f'val : {val}')

        dp[start][end] = min(tmp)

print(dp[0][n-1])
# print(dp)