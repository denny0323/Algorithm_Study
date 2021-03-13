'''
> Problem
@ 백준 Class3 1260번
@ DFS와 BFS
@ URL https://www.acmicpc.net/problem/1260
'''

#input_file = open('./input/1260(1).txt', 'r')
#input = input_file.readline

import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    if j not in graph[i]:
        graph[i].append(j); graph[j].append(i)
graph = [sorted(i) for i in graph]
        
        
visited_dfs = [0 for _ in range(N+1)]
result_dfs = []
def dfs(n):
    visited_dfs[n] = 1
    result_dfs.append(str(n))
    for child in graph[n]:
        if not visited_dfs[child]:
            dfs(child)

result_bfs = []
def bfs(n):
    visited = [0 for _ in range(N+1)]
    q = deque()
    q.append(n)
    visited[n] = 1
    while q:
        x = q.popleft()
        result_bfs.append(str(x))
        for child in graph[x]:
            if not visited[child]:
                q.append(child)
                visited[child] = 1

dfs(V)
bfs(V)

print(' '.join(result_dfs))
print(' '.join(result_bfs))

'''
> result 
@ Memory : 34000 KB
@ Time : 112 ms
@ Code length : 912 B
'''

