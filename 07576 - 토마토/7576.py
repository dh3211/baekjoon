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

run_baekjoon(5, __file__)
##############################################################################
##############################################################################

from queue import Queue
import sys

n, m = list(map(int, sys.stdin.readline().split(' ')))

q = Queue()

MAP = [[-1 for _ in range(n+2)] for _ in range(m+2)]
for j in range(m):
    MAP_row = list(map(int, sys.stdin.readline().split(' ')))
    for i in range(n):
        MAP[j+1][i+1] = MAP_row[i]
        if MAP_row[i]==1:
            q.put([i+1,j+1])


while not q.empty():
    x,y = q.get()
    val = MAP[y][x]

    for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
        X = x+dx
        Y = y+dy

        if MAP[Y][X] != 0:
            continue
        
        MAP[Y][X] = val+1
        q.put([X,Y])

raw_tomato = False
for j in range(1,m+2):
    for i in range(1,n+2):
        if MAP[j][i] == 0:
            raw_tomato = True

if raw_tomato:
    print(-1)
else:
    print(val-1)