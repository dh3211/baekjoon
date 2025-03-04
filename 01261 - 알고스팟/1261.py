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

from queue import Queue
import sys


n,m = list(map(int, sys.stdin.readline().split(' ')))

MAP = [[-1 for _ in range(n+2)] for _ in range(m+2)]
for j in range(m):
    MAP_row = sys.stdin.readline().strip()
    MAP_row = list(map(int, list(MAP_row)))
    for i in range(n):
        MAP[j+1][i+1] = MAP_row[i]

visited = [[False for _ in range(n+2)] for _ in range(m+2)]
visited[1][1] = True

dp = [[0 for _ in range(n+2)] for _ in range(m+2)]


q = Queue()
q.put([1,1])

while not q.empty():
    x,y = q.get()
    val = dp[y][x]
    
    for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
        X = x+dx
        Y = y+dy

        if MAP[Y][X] == -1:
            continue
        if visited[Y][X] and dp[Y][X] <= val +MAP[Y][X]:
            continue
        
        dp[Y][X] = val +MAP[Y][X]
        visited[Y][X] = True
        q.put([X,Y])

ans = dp[m][n]
print(ans)
    

    


    
