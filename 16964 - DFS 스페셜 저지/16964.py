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

import sys


n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = list(map(int, sys.stdin.readline().split(' ')))
    graph[a].append(b)
    graph[b].append(a)

input_ans = list(map(int, sys.stdin.readline().split(' ')))

input_order = {}
for idx, node in enumerate(input_ans):
    input_order[node] = idx

def DFS(node):
    my_ans.append(node)
    
    graph[node].sort(key= lambda x : input_order[x] )
    for nd in graph[node]:
        if check[nd]:
            continue
        
        check[nd] = True
        DFS(nd)

my_ans = []
check = [False]*(n+1)
check[1] = True
DFS(1)

correct = 1
for input_, my_ in zip(input_ans, my_ans):
    if input_ == my_:
        continue

    correct = 0
    break

print(correct)

