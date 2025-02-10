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

n = int(sys.stdin.readline())
work_table = []
for _ in range(n):
    day, money = map(int, sys.stdin.readline().split(' '))
    work_table.append([day, money])

dp = [0 for _ in range(n+60)]
mx = 0
for i, (day, money) in enumerate(work_table):
    mx = max(mx, dp[i])
    dp[i+day] = max(mx + money, dp[i+day])

ans = max(dp[:n+1])
print(ans)