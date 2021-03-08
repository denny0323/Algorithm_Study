'''
> Problem
@ 백준 Class3 2606번
@ 바이러스
@ URL https://www.acmicpc.net/problem/2606
'''

import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
pairs = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(pairs):
    i, j = map(int, input().split())
    graph[i].append(j); graph[j].append(i)

virus_exist = [0] * (N+1)
virus_exist[1] = 1

############################## BFS ##############################

def bfs(graph):
    q = deque()
    q.append(1)
    count = 0

    while q:
        curr = q.popleft()
        for child in graph[curr]:
            if virus_exist[child] == 0:
                q.append(child)
                count += 1
                virus_exist[child] = 1
    print(count)
bfs(graph)

'''
> result 
@ Memory : 31736 KB
@ Time : 96 ms
@ Code length : 909 B
'''

############################## DFS ##############################
def dfs(graph):
    q = deque()
    q.append(1)
    count = 0

    while q:
        curr = q.pop()
        for child in graph[curr]:
            if virus_exist[child] == 0:
                q.append(child)
                count += 1
                virus_exist[child] = 1
    print(count)
dfs(graph)
    
'''
> result 
@ Memory : 31736 KB
@ Time : 92 ms
@ Code length : 909 B
'''
