'''
> Problem
@ 백준 Class4 2263번
@ 트리의 순회
@ URL https://www.acmicpc.net/problem/2263
'''

import sys
sys.setrecursionlimit(10 ** 6)

def divide_tree(in_l, in_r, post_l, post_r): # inorder의 어디부터 어디까지를 왼쪽/오른쪽 sub tree으로 볼것이며, 
                                             # postorder의 어디부터 어디까지를 왼쪽/오른쪽 sub tree으로 볼것인지 정함. 즉, slicing하는 것.
    
    if in_l > in_r or post_l > post_r:
        return

    root = postorder[post_r]  # postorder에서는 항상 맨 뒤(즉 맨 오른쪽)의 index가 subtree의 root
    #print(in_l, in_r, post_l, post_r, root)  # 종결 조건이 유효한지 보자.
    print(root, end=" ")      # 뽑자
    idx_root = in_idx[root]  # root의 index를 inorder에서 찾으면

    left_cnt = idx_root-in_l 
    right_cnt = in_r-idx_root

    divide_tree(      in_l, idx_root-1,           post_l, post_l+left_cnt-1) # pre에선 왼쪽먼저
    divide_tree(idx_root+1,       in_r, post_r-right_cnt,          post_r-1)

    
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# Guide : https://developmentdiary.tistory.com/439
# 중위순회과 후위순회을 그려보면 규칙을 찾을 수 있다. 
# 후위 탐색된 리스트에서 맨 마지막 값은 중위 순회의 루트노드일 것이다.
# 따라서 중위 탐색에서 그 루트노드의 인덱스를 구해서 왼쪽 오른쪽 나눠서 
# 재귀적인 문제로 만들어 풀면 된다.

# postorder를 참조하여 바꾸되, inorder를 지표삼아 좌우를 구분한다.
in_idx = [0 for _ in range(n+1)] # inorder를 지표 삼기위해 각 node가 inorder에 몇번째 index에 있는가?
for i in range(n):
    in_idx[inorder[i]] = i # inorder의 i번째는 n이다. <=> node n은 inorder에서 i번째 index이다. (in_idx[n]=i)
    
divide_tree(0, n-1, 0, n-1)
    
'''
> result 
@ Memory : 138192 KB
@ Time : 312 ms
@ Code length : 683 B (주석포함 1320 B)
'''