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

num_li = []
for _ in range(9):
    num = int(sys.stdin.readline())
    num_li.append(num)

def find(li, sum, n, idx, num_li):
    if sum==100 and n ==7:
        return li
    
    elif sum >=100:
        return None
    
    elif idx >= 10:
        return None
    
    elif n >= 7:
        return None
    

    idx_ = idx
    for e in num_li[idx:]:
        li_ = li[:]
        li_.append(e)
        idx_ +=1

        ans = find(li_, sum +e, n+1, idx_, num_li)

        if ans:
            return ans
        
ans_li = find([], 0, 0, 0, num_li)
for e in ans_li:
    print(e)