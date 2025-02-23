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

while True:
    n, m = map(int, sys.stdin.readline().split())
    if n==0 and m==0:
        break
    
    map_ = [[0] * (n+2) ]
    for _ in range(m):
        input_map = list(map(int, sys.stdin.readline().split(' ')))
        map_li = [0] + input_map + [0]
        map_.append(map_li)
    map_.append([0] * (n+2))

    ans = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if map_[j][i] ==0:
                continue
            
            ans +=1
            q = Queue()
            q.put([i,j])
            while not q.empty():
                i_, j_ = q.get()
                if map_[j_][i_] ==0:
                    continue

                map_[j_][i_] = 0

                for a in [-1,0,1]:
                    for b in [-1,0,1]:
                        q.put([i_ +a, j_ +b] )

    print(ans)
