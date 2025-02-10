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
q.put(n)

li = [-1] *(n+1)
li[n] = 0



def func(kg, ea):
    if kg < 0:
        pass
    elif li[kg] == -1:
        li[kg] = ea
        q.put(kg)
    elif li[kg] > ea:
        li[kg] = ea
        q.put(kg)

while not q.empty():
    kg = q.get()
    ea = li[kg]

    func(kg -5, ea+ 1)
    func(kg -3, ea+ 1)

    if li[0] != -1:
        break

print(li[0])
    
    


