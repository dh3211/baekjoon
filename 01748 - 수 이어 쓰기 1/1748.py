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

N = int(sys.stdin.readline())
ans = [0]
def find(n,i):
    c = 9*10**(i)
    if n < c:
        ans[0] += n*(i+1)

    else:
        ans[0] += c*(i+1)
        find(n- c, i+1)

find(N,0)
print(*ans)
