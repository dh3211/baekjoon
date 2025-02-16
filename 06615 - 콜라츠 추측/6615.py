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

while 1:
    A, B = list(map(int, sys.stdin.readline().split(' ')))
    if A==0 and B==0:
        break
    a = A
    b = B
    a_li = [a]
    b_li = [b]
    while a != 1:
        if a%2 == 0:
            a = a//2
        else:
            a = 3*a +1
        a_li.append(a)

    while b != 1:
        if b%2 == 0:
            b = b//2
        else:
            b = 3*b +1
        b_li.append(b)

    a_set = set(a_li)
    for b_ele in b_li:
        if b_ele in a_set:
            C = b_ele
            break
    
    # print('')
    # print(a_li)
    # print(b_li)
    
    sa = a_li.index(C)
    sb = b_li.index(C)

    print(f"{A} needs {sa} steps,", end=' ')
    print(f"{B} needs {sb} steps,", end=' ')
    print(f"they meet at {C}")
    