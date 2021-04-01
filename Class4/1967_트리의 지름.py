'''
> Problem
@ 백준 Class4 1967번
@ 트리의 지름
@ URL https://www.acmicpc.net/problem/1967
'''


# __트리의 지름__은 임의의 하나의 노드 A에서 가장 거리가 먼 노드 B를 구하고  
# 이 노드 B에서 가장 거리가 먼 노드 C를 구하게 되었을 때, B와 C 사이의 거리

import sys
input = sys.stdin.readline

# input_file = open('./input/1967.txt', 'r')
# input = input_file.readline

N = int(input())
Tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    p, c, w = list(map(int, input().split()))
    Tree[p].append((w, c)); Tree[c].append((w, p));

def max_dist(node):
    dist = [-1] * (N+1)
    dist[node] = 0
    max_dist = -1
    max_node = 0
    
    q = []
    q.append(node)
    
    while q:
        n = q.pop()
        
        for w_c, n_c in Tree[n]:
            # 거리 update
            if dist[n_c] == -1: # 방문 안했음.
                dist[n_c] = dist[n] + w_c
                q.append(n_c)
                
                if dist[n_c] > max_dist: # check max_node and max_dist  
                    max_dist = dist[n_c]
                    max_node = n_c
    return max_dist, max_node

_, max_n = max_dist(1)
rad, _ = max_dist(max_n)
print(rad)

'''
> result : 틀렸습니다(100%)
-> N=1일때 예외 처리
'''

import sys
input = sys.stdin.readline

N = int(input())
Tree = [[] for _ in range(N+1)]

if N == 1:
    print(0)
    
else: 
    for _ in range(N-1):
        p, c, w = list(map(int, input().split()))
        Tree[p].append((w, c)); Tree[c].append((w, p));

    def max_dist(node):
        dist = [-1] * (N+1)
        dist[node] = 0
        max_dist = -1
        max_node = 0

        q = []
        q.append(node)

        while q:
            n = q.pop()

            for w_c, n_c in Tree[n]:
                # 거리 update
                if dist[n_c] == -1: # 방문 안했음.
                    dist[n_c] = dist[n] + w_c
                    q.append(n_c)

                    if dist[n_c] > max_dist: # check max_node and max_dist  
                        max_dist = dist[n_c]
                        max_node = n_c
        return max_dist, max_node

    _, max_n = max_dist(1)
    rad, _ = max_dist(max_n)
    print(rad)

'''
> result 
@ Memory : 31844 KB
@ Time : 104 ms
@ Code length : 924 B
'''

