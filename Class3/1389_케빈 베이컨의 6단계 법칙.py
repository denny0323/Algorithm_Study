'''
> Problem
@ 백준 Class3 1389번
@ 케빈 베이컨의 6단계 법칙
@ URL https://www.acmicpc.net/problem/1389
'''
# from collections import deque

# input_file = open('./input/1389.txt', 'r')
# input = input_file.readline

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    if j not in graph[i]:
        graph[i].append(j); graph[j].append(i)

def bfs(n, lvl=1):
    q = deque()
    q.append((n,0))
    visited[n] = 1
    while q:
        x, lvl = q.popleft()
        for child in graph[x]:
            if not visited[child]:
                q.append((child, lvl+1))
                bacon[child] = lvl+1
                visited[child] = 1

kebinbacons=[]
for i in range(1, N+1):
    bacon = [0 for _ in range(N+1)]
    visited = [0 for _ in range(N+1)] 
    bfs(i)
    kebinbacons.append((i, sum(bacon)))
kebinbacons.sort(key=lambda x:(x[1], x[0]))

print(kebinbacons[0][0])

'''
> result 
@ Memory : 32052 KB
@ Time : 88 ms
@ Code length : 796 B
'''

