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
li = list(map(int, sys.stdin.readline().split(' ')))
li = [0] +li
ans_li = [0]
for idx in range(1,n+1):
    tmp_idx_li = []
    for i in range(idx):
        if li[i] < li[idx]:
            tmp_idx_li.append(i)
    # print(tmp_idx_li)
    tmp_ele_li = []
    for i in tmp_idx_li:
        tmp_ele_li.append(ans_li[i])

    ans_li.append(max(tmp_ele_li) +1)

    # print(ans_li)
print(max(ans_li))
        
