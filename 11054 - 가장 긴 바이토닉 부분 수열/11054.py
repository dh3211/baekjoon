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
li = [0] + li
idx_ele = []
for idx, ele in enumerate(li):
    idx_ele.append([idx,ele])

up_li = [0]
for idx, ele in idx_ele[1:]:
    small_list = filter(lambda x : x[1] < ele, idx_ele[:idx])
    small_idx = map(lambda x : x[0], small_list)
    
    best_val = [up_li[i] for i in small_idx]

    up_li.append(max(best_val) +1)


dn_li = [0]
idx_ele[0][1]=1001
for idx, ele in idx_ele[1:]:
    big_list = filter(lambda x : x[1] > ele, idx_ele[:idx])
    big_idx = list(map(lambda x : x[0], big_list))

    best_val_1 = [up_li[i] for i in big_idx]
    best_val_2 = [dn_li[i] for i in big_idx]
    best_val = best_val_1 + best_val_2

    dn_li.append(max(best_val) +1)

ans = max(up_li + dn_li)

print(ans)
