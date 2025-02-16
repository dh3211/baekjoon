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

n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, d = map(int, sys.stdin.readline().split(' '))

    tree[a].append([b, d])
    tree[b].append([a, d])


ans = 0

from queue import Queue
check_set = set([1])
q = Queue()
q.put([1, 0])
while not q.empty():
    room, distance = q.get()
    for rm, di in tree[room]:
        if rm in check_set:
            continue

        q.put([rm, distance +di])
        check_set.add(rm)
        ans = max(ans, distance +di)

print(ans)



