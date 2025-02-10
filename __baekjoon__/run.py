import sys
import os
import atexit
import os
import time



def run_baekjoon(n, file_path):
    print('---------------------------------------------------------------------')
    print('my ans:')
    id = os.path.basename(file_path).replace('.py','')
    dir_path = os.path.dirname(file_path)
    IOfolder_path = os.path.join(dir_path,"IO")
    input_file  = os.path.join(IOfolder_path, f'{id}_{n}_i.txt')
    output_file = os.path.join(IOfolder_path, f'{id}_{n}_o.txt')



    sys.stdin = open(input_file, "r")
    start = time.time() 
    atexit.register(lambda: print_ans(output_file, start))


def print_ans(output_file, start):
    now = time.time()
    print()
    print('ans:')
    with open(output_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 각 줄 출력
    for line in lines:
        print(line.strip())

    print()
    print(f'time: {now- start :.4f}')
