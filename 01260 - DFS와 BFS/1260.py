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

node_count, line_count, root_node =\
    map(int, sys.stdin.readline().split(' '))

graph = [[0 for _ in range(node_count+1)] for _ in range(node_count +1)]
for _ in range(line_count):
    a, b = map(int, sys.stdin.readline().split(' '))
    graph[a][b] = 1
    graph[b][a] = 1

  # dfs
dfs_check = [0] *(node_count+1)
dfs_check[root_node] = 1
dfs_ans = []

def dfs(point):
    if dfs_check == 1:
        return
    
    for idx in range(1, node_count+1):
        if graph[point][idx] == 0:
            continue
        if dfs_check[idx] == 1:
            continue
        
        dfs_check[idx] = 1
        dfs_ans.append(idx)
        dfs(idx)

dfs_ans.append(root_node)
dfs(root_node)

  # bfs
bfs_check = [0] *(node_count+1)
bfs_ans = []

q = Queue()
q.put(root_node)

while not q.empty():
    point = q.get()
    if bfs_check[point] == 1:
        continue
    
    bfs_ans.append(point)
    bfs_check[point] = 1

    for idx in range(1, node_count+1):
        if graph[point][idx] == 0:
            continue

        q.put(idx)

print(*dfs_ans)
print(*bfs_ans)