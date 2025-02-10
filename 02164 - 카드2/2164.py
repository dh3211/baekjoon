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
import queue

n = int(sys.stdin.readline())

q = queue.Queue()
for i in range(1, n +1):
    q.put(i)

for _ in range(n-1):
    q.get()
    ele = q.get()
    q.put(ele)

print(q.get())



