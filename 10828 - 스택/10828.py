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

class Stack():
    def __init__(self):
        self.node = None
        self.num = 0

    def push(self, X):
        self.new = Node(X)
        self.new.next =self.node
        self.node = self.new
        self.num +=1

    def pop(self):
        if self.node:
            print(self.node.data)
            self.node = self.node.next
            self.num -=1

        else:
            print(-1)

    def size(self):
        print(self.num)

    def empty(self):
        if self.node:
            print(0)
        else:
            print(1)

    def top(self):
        if self.node:
            print(self.node.data)
        else:
            print(-1)

stack = Stack()

n = int(sys.stdin.readline())
for _ in range(n):
    s = sys.stdin.readline().strip()
    if s == 'top':
        stack.top()
    elif s == 'size':
        stack.size()
    elif s == 'pop':
        stack.pop()
    elif s == 'empty':
        stack.empty()
    else:
        x = int(s.split(' ')[1])
        stack.push(x)


        


