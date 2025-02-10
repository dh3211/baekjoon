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
        self.prev = None

class Deque():
    def __init__(self):
        self.first_node = None
        self.last_node = None
        self.num = 0

    def push_front(self, X):
        new_node = Node(X)
        if self.first_node:
            self.first_node.prev = new_node
            new_node.next = self.first_node
            self.first_node = new_node
        else:
            self.first_node = new_node
            self.last_node  = new_node

        self.num +=1

    def push_back(self, X):
        new_node = Node(X)
        if self.first_node:
            self.last_node.next = new_node
            new_node.prev = self.last_node
            self.last_node =new_node
        else:
            self.first_node = new_node
            self.last_node  = new_node

        self.num +=1

    def pop_front(self):
        if self.first_node:
            print(self.first_node.data)

            if self.first_node.next:
                self.first_node = self.first_node.next
                self.first_node.prev = None
                self.num -=1
            else:
                self.first_node = None
                self.last_node = None
                self.num = 0
        else:
            print(-1)


    def pop_back(self):
        if self.first_node:
            print(self.last_node.data)

            if self.last_node.prev:
                self.last_node = self.last_node.prev
                self.last_node.next = None
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


deque = Deque()

n = int(sys.stdin.readline())
for _ in range(n):
    s = sys.stdin.readline().strip()
    if s == 'front':
        deque.front()
    elif s == 'back':
        deque.back()
    elif s == 'size':
        deque.size()
    elif s == 'empty':
        deque.empty()
    elif 'push' in s:
        X = int(s.split(' ')[1])
        if 'front' in s:
            deque.push_front(X)
        else:
            deque.push_back(X)
    elif 'pop' in s:
        if 'front' in s:
            deque.pop_front()
        else:
            deque.pop_back()
