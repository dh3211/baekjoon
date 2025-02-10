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

#ele = [마지막줄 0마리, 왼쪽 1마리, 오른쪽 한마리]
lili = [[0,0,0],
        [1,1,1]]
for idx in range(2, n+1):
    ele_00, ele_10, ele_01 = lili[-1]
    li = []
    val_00 = ele_00 + ele_01 + ele_10
    li.append(val_00 % 9901)

    val_10 = ele_00 + ele_01
    li.append(val_10 % 9901)

    val_01 = ele_00 + ele_10
    li.append(val_01 % 9901)

    lili.append(li)

ans = sum(lili[-1]) % 9901
print(ans)