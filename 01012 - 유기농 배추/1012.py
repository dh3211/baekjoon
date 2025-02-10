'''
int(sys.stdin.readline())
sys.stdin.readline().strip()
map(int, sys.stdin.readline().split(' '))
list(map(int, sys.stdin.readline().split(' ')))
'''
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from __baekjoon__.run import run_baekjoon
run_baekjoon(1, __file__)
##############################################################################
##############################################################################
from collections import deque
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    m, n, k = list(map(int, sys.stdin.readline().split(' ')))
    map_lili = [[0 for j in range(m+2)] for i in range(n+2)]
    coor_li = [0]
    for idx in range(1,k+1):
        x, y = list(map(int, sys.stdin.readline().split(' ')))
        x +=1
        y +=1
        map_lili[y][x] = idx
        coor_li.append([x,y])

    ans = 0
    check = [False] *(k+1)
    deq = deque(coor_li[1:])
    while deq:
        X,Y = deq.popleft()
        IDX = map_lili[Y][X]
        if check[IDX]==True:
            continue

        ans +=1

        deq_2 = deque()
        deq_2.append([X,Y])
        while deq_2:
            x,y = deq_2.popleft()

            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                idx = map_lili[y+dy][x+dx]
                if idx ==0:
                    continue
                
                if check[idx] == False:
                    check[idx] = True
                    deq_2.appendleft([x+dx, y+dy])
                
    print(ans)