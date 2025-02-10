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

n = int(sys.stdin.readline())
q = Queue()
li = [-1] * (n+1)

q.put(n)
li[n] = 0


def fun(n, v):
    if li[n] ==-1:
        li[n] = v
        q.put(n)

    elif li[n] > v:
        li[n] = v
        q.put(n)



while not q.empty():
    n = q.get()
    v = li[n]


    if n%3==0:
        fun(n//3, v+1)

    if n%2==0:
        fun(n//2, v+1)

    if n!=1:
        fun(n-1, v+1)

    if n==1:
        break

print(li[1])