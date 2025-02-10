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

from queue import Queue
import sys

n = int(sys.stdin.readline())
n = n-1

li = [[] for _ in range(n+2)]
for _ in range(n):
    a, b = list(map(int, sys.stdin.readline().split(' ')))
    li[a].append(b)
    li[b].append(a)


ans = [0] *(n+2)
ans[1] = 1
q = Queue()
q.put(1)
while not q.empty():
    ele = q.get()
    for node in li[ele]:
        if ans[node] ==0:
            ans[node] = ele
            q.put(node)
        
for a in ans[2:]:
    print(a)



