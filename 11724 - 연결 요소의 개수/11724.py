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

run_baekjoon(2, __file__)
##############################################################################
##############################################################################

import sys
from queue import Queue


N, M = map(int, sys.stdin.readline().split(' '))
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split(' '))
    graph[a].append(b)
    graph[b].append(a)


ans = 0
check = [0] *(N+1)
for root in range(1, N+1):
    if check[root] == 1:
        continue

    ans+=1
    check[root] = 1

    q = Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        
        check[node] = 1
        for nd in graph[node]:
            if check[nd] == 1:
                continue

            q.put(nd)
            check[nd] = 1

print(ans)

