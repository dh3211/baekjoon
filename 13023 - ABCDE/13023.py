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

run_baekjoon(4, __file__)
##############################################################################
##############################################################################

import sys
from queue import Queue


N, M = list(map(int, sys.stdin.readline().split(' ')))

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = list(map(int, sys.stdin.readline().split(' ')))
    graph[a].append(b)
    graph[b].append(a)


ans = [0]


def dfs(node, count):
    if count ==5:
        ans[-1] = 1
        return
    if ans[-1] == 1:
        return

    for nd in graph[node]:
        if check[nd] == True:
            continue

        check[nd] = True
        dfs(nd, count+1)
        check[nd] = False

check = [False]*N
for node in range(N):
    check[node] = True
    dfs(node, 1)
    check[node] = False
    
print(*ans)