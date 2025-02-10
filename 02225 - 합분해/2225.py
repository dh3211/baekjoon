import sys
import os
module_path =\
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(module_path)
from __baekjoon__ import run_baekjoon

'''
int(sys.stdin.readline())
sys.stdin.readline().strip()
map(int, sys.stdin.readline().split(' '))
list(map(int, sys.stdin.readline().split(' ')))
'''

run_baekjoon(2, __file__)
##############################################################################
##############################################################################
#     | 0 1 2 3 4 5 6 7 8 9
# k=1 | 1 1 1 1 1 1 1 1 1 1
# k=2 | 1 2 3 4 5 6 7 8 9 10
# k=3 | 1 3 6 10
import sys

N, K = map(int, sys.stdin.readline().split(' '))
lili = [
        [1] *(N+1)
        ]
for k in range(2, K+1):
    li = [1]
    for n in range(1,N+1):
        val = li[-1] +lili[-1][n]
        val = val%1000000000
        li.append(val)
    lili.append(li)

ans = lili[-1][-1]
print(ans)