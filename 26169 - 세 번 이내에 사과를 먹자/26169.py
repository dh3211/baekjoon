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
import copy
from queue import Queue


MAP = [[-1 for _ in range(7)] for _ in range(7)]
for j in range(5):
    input_map = list(map(int, sys.stdin.readline().split(' ')))
    for i in range(5):
        MAP[j+1][i+1] = input_map[i]


r, c = map(int, sys.stdin.readline().split(' '))
r +=1
c +=1

move_count = 0
apple_count = 0

ans = 0
q = Queue()
q.put([r,c, MAP, move_count, apple_count])
while not q.empty():
    y, x, MAP, move_count, apple_count = q.get()
    copyed_MAP = copy.deepcopy(MAP)

    if copyed_MAP[y][x] == 1:
        apple_count +=1
    copyed_MAP[y][x] = -1
    # print(x, y, move_count, apple_count)
    # for li in copyed_MAP:
    #     print(li)
    if apple_count >=2:
        ans = 1
        # print(apple_count)
        # print(move_count)
        # print(x,y)
        break
    

    for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
        new_x = x+dx
        new_y = y+dy

        if copyed_MAP[new_y][new_x] == -1:
            continue
        if move_count >=3:
            continue

        q.put([new_y, new_x, copyed_MAP, move_count +1, apple_count])
        

print(ans)
        
