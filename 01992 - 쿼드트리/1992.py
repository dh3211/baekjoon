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

mp= []
for i in range(n):
    li = sys.stdin.readline().strip()
    li = list(li)

    mp.append(li +[])

mpli= []
mpli.append(mp)



def make(n, mpli):
    n = n//2
    
    if n<1:
        return 1, mpli
    
    target = mpli[-1]
    mp = []
    for i in range(n):
        li = []
        for j in range(n):
            a = target[i*2][j*2]
            b = target[i*2][j*2+1]
            c = target[i*2+1][j*2]
            d = target[i*2+1][j*2+1]

            ele = f"({a}{b}{c}{d})"

            if ele =='(0000)':
                ele = '0'
            elif ele =='(1111)':
                ele = '1'

            li.append(ele)
        mp.append(li)
    mpli.append(mp)

    return make(n, mpli)
    

n, mpli = make(n, mpli)

print(mpli[-1][0][0])