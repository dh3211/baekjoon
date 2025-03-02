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
from queue import Queue


N, K = map(int, sys.stdin.readline().split(' '))
MAX = max(N,K)
dp = [0] *(MAX*2+1)
end = 0

if N==K:
    print(0)

else:
    q = Queue()
    q.put(N)
    while not q.empty():
        idx = q.get()

        for new_idx in [idx+1, idx-1, idx *2]:
            if new_idx > (MAX*2+1):
                continue
            if new_idx < 0:
                continue
            if dp[new_idx] != 0:
                continue

            q.put(new_idx)
            dp[new_idx] = dp[idx] +1

            if K == new_idx:
                end = 1

        if end:
            break
    

    print(dp[K])
        