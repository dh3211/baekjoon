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


N = int(sys.stdin.readline())
MAP = [[0 for _ in range(N+2)] for _ in range(N+2)]
for j in range(N):
    tmp = sys.stdin.readline().strip()
    tmp = list(tmp)
    tmp = list(map(int, tmp) )
    for i in range(N):
        MAP[j+1][i+1] = tmp[i]

group = 0
group_counts = []

for j in range(1, N+2):
    for i in range(1, N+2):
        if MAP[j][i] == 0:
            continue
        
        group +=1
        group_counts.append(1)
        MAP[j][i] = 0
        q = Queue()
        q.put([i, j])

        while not q.empty():
            x, y = q.get()
            
            for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
                if MAP[y+dy][x+dx] ==0:
                    continue

                group_counts[-1] +=1
                MAP[y+dy][x+dx] =0
                q.put([x+dx, y+dy])
        

print(group)
group_counts.sort()
for ele in group_counts:
    print(ele)