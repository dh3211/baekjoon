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

m, n = list(map(int, sys.stdin.readline().split(' ')))

map_ = [['.'] * (n+2)]
for _ in range(m):
    map_part = ['.'] + list(sys.stdin.readline().strip()) + ['.']
    map_.append(map_part)
map_.append(['.'] * (n+2))

ans = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if map_[j][i] == '.':
            continue
        
        ans +=1 

        q = Queue()
        q.put([i,j])
        while not q.empty():
            i_, j_ = q.get()
            if map_[j_][i_] == '.':
                continue
            
            map_[j_][i_] = '.'

            for di in [-1,0,1]:
                for dj in [-1, 0, 1]:
                    if di*dj != 0:
                        continue

                    q.put([i_ + di, j_ + dj])

print(ans)