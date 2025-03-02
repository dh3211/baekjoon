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


N = int(sys.stdin.readline())
A, B = map(int, sys.stdin.readline().split(' '))
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split(' '))
    graph[a].append(b)
    graph[b].append(a)

ans = -1
q = Queue()
q.put([A,0])
check = [False] *(N+1)
check[A] = True

while not q.empty():
    node, count = q.get()
    if node == B:
        ans = count
        break

    for nd in graph[node]:
        if check[nd] == True:
            continue

        q.put([nd, count +1])
        check[nd] = True        

print(ans)

