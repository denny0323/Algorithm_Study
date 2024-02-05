'''
> Problem
@ 백준 Class4 5639번
@ 이진 검색 트리
@ URL https://www.acmicpc.net/problem/2683
'''

### 풀이 참고 (https://backtony.github.io/algorithm/2021/02/18/algorithm-boj-class4-20/)

def post_order(start, end):
    # 역전시 리턴
    if start > end:
        return

    # root
    root = pre_order[start]
    
    # root의 다음부터 찾고
    idx = start + 1
    ## root보다 커지는 지점으로 update
    while idx <= end:
        if pre_order[idx] > root:
            break
        idx += 1

    # 왼쪽 서브트리
    post_order(start + 1, idx - 1)

    # 오른쪽 서브트리
    post_order(idx, end)

    # 후위순회이므로 제일 마지막에 print
    print(root)

import sys
sys.setrecursionlimit(10 ** 9)
#sys.stdin = open('./input/5639.txt', 'r')
input = sys.stdin.readline

pre_order = []
while True:
    try:
        pre_order.append(int(input()))
    except:
        break

post_order(0, len(pre_order) - 1)

'''
> result 
@ Memory : 38028 KB
@ Time : 4228 ms
@ Code length : 734 B
'''

