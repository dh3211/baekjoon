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

rip_tomatos_lists = []
rip_tomatos = []
tomato_count = 0
rip_tomato_count = 0

MAP = [[-1 for _ in range(n+2)] for _ in range(m+2)]
for j in range(m):
    MAP_row = list(map(int, sys.stdin.readline().split(' ')))
    for i in range(n):
        MAP[j+1][i+1] = MAP_row[i]

        if MAP_row[i] != -1:
            tomato_count+=1

        if MAP_row[i]==1:
            rip_tomatos.append([i+1,j+1])
            rip_tomato_count+=1

rip_tomatos_lists.append(rip_tomatos)


step =-1
ing = True

while ing:
    step+=1
    ing = False

    rip_tomatos = []
    for x,y in rip_tomatos_lists[-1]:
        val = MAP[y][x]

        for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
            X = x+dx
            Y = y+dy

            if MAP[Y][X] != 0:
                continue
            
            ing = True
            MAP[Y][X] = 1
            rip_tomato_count +=1
            rip_tomatos.append([X,Y])

    rip_tomatos_lists.append(rip_tomatos)


if tomato_count == rip_tomato_count:
    print(step)
else:
    print(-1)