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
from collections import deque


n = int(sys.stdin.readline())
di_c_left = {'.':'.'}
di_c_righ = {'.':'.'}

di_p = {'A' : ''}
left_leaf = []

leaf_num = {}

for _ in range(n):
    st = sys.stdin.readline().strip()
    p, c1 ,c2 = st.split(' ')

    di_p[c1] = p
    di_p[c2] = p

    di_c_left[p] = c1
    di_c_righ[p] = c2
            

#######   1   ##################
ans = []
check = set()
check.add('.')
deq = deque()
deq.append('A')
while deq:
    ele = deq.popleft()

    if ele == '.':
        continue

    left = di_c_left[ele]
    righ = di_c_righ[ele]

    if left in check and righ in check:
        ans.append(ele)
        continue

    deq.appendleft(righ)
    deq.appendleft(left)
    deq.appendleft(ele)
    check.add(ele)
    check.add(righ)
    check.add(left)

print(''.join(ans))
#######   2   ##################
ans = []
check = set()
check.add('.')
deq = deque()
deq.append('A')
while deq:
    ele = deq.popleft()

    if ele == '.':
        continue

    left = di_c_left[ele]
    righ = di_c_righ[ele]

    if left in check and righ in check:
        ans.append(ele)
        continue

    deq.appendleft(righ)
    deq.appendleft(ele)
    deq.appendleft(left)
    check.add(ele)
    check.add(righ)
    check.add(left)

print(''.join(ans))

#######   3   ##################
ans = []
check = set()
check.add('.')
deq = deque()
deq.append('A')
while deq:
    ele = deq.popleft()

    if ele == '.':
        continue

    left = di_c_left[ele]
    righ = di_c_righ[ele]

    if left in check and righ in check:
        ans.append(ele)
        continue

    deq.appendleft(ele)
    deq.appendleft(righ)
    deq.appendleft(left)
    check.add(ele)
    check.add(righ)
    check.add(left)

print(''.join(ans))

        


