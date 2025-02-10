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

run_baekjoon(2, __file__)
##############################################################################
##############################################################################

# 9 10 -99 19 30 49 -1000 100 200
import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split(' ')))

default_li = [0]
remove_li = [0]

for ele in li:
    old_default = default_li[-1]
    cur_default = old_default + ele

    new_default = max(cur_default, 0)
    default_li.append(new_default)

    cur_remove = old_default
    old_remove = remove_li[-1] + ele
    
    new_remove = max(cur_remove, old_remove)
    remove_li.append(new_remove)

if max(li) > 0:
    ans = max(default_li +remove_li )
    print(ans)

else:
    print(max(li))