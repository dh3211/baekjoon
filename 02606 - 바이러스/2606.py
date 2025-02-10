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
l = int(sys.stdin.readline())

com_li = [0] *(n+1)
link_gp = [[] for _ in range(n+1)]
for _ in range(l):
    a, b = map(int, sys.stdin.readline().split(' '))
    link_gp[b].append(a)
    link_gp[a].append(b)

ans = 0
check = [False] *(n+1)
check[1] = True
q = Queue()
q.put(1)
while not q.empty():
    ele = q.get()
    for e in link_gp[ele]:
        if check[e] ==False:
            check[e] = True
            q.put(e)
            ans +=1

print(ans)
