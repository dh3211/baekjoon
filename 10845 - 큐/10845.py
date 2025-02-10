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


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.first_node = None
        self.last_node = None
        self.num = 0

    def push(self, X):
        new_node = Node(X)
        if self.first_node:
            self.last_node.next = new_node
            self.last_node =new_node
        else:
            self.first_node = new_node
            self.last_node  = new_node

        self.num +=1

    def pop(self):
        if self.first_node:
            print(self.first_node.data)
            if self.first_node.next:
                self.first_node = self.first_node.next
                self.num -=1
            else:
                self.first_node = None
                self.last_node = None
                self.num = 0
        else:
            print(-1)

    def size(self):
        print(self.num)

    def empty(self):
        if self.first_node:
            print(0)
        else:
            print(1)

    def front(self):
        if self.first_node:
            print(self.first_node.data)
        else:
            print(-1)

    def back(self):
        if self.first_node:
            print(self.last_node.data)
        else:
            print(-1)


queue = Queue()

n = int(sys.stdin.readline())
for _ in range(n):
    s = sys.stdin.readline().strip()
    if s == 'front':
        queue.front()
    elif s == 'back':
        queue.back()
    elif s == 'size':
        queue.size()
    elif s == 'pop':
        queue.pop()
    elif s == 'empty':
        queue.empty()
    else:
        x = int(s.split(' ')[1])
        queue.push(x)

