'''
> Problem
@ 백준 Class3 11724번
@ 연결 요수의 개수
@ URL https://www.acmicpc.net/problem/11724
'''
############################## DFS ##############################

import sys
input = sys.stdin.readline

# python은 재귀제한이 걸려있기 때문에 재귀 허용치가 넘어가면 런타임에러가 발생한다.
# (기본적으로 설정되있는 최대 재귀 깊이는 1,000.) 이러한 이유 때문에 재귀 허용치를 늘려줌
# source : https://pilyeooong.tistory.com/entry/백준-11724번-연결-요소의-개수-Python-파이썬-백준-알고리즘
sys.setrecursionlimit(10000)

N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    graph[i-1].append(j-1); graph[j-1].append(i-1)

visited = [0] * N

def dfs(i):
    visited[i] = 1
    for child in graph[i]:
        if not visited[child]:
            dfs(child) 
            
link = 0
for i in range(N):    
    if not visited[i]:
        dfs(i)
        link +=1
print(link)

'''
> result 
@ Memory : 63600 KB
@ Time : 876 ms
@ Code length : 485 B
'''


############################## BFS ##############################

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    graph[i-1].append(j-1); graph[j-1].append(i-1)

visited = [0] * N

def bfs(i):
    q = deque()
    q.append(i)
    while q:
        curr = q.popleft()
        for child in graph[curr]:
            if not visited[child]:
                q.append(child)
                visited[child] = 1
            
link = 0
for i in range(N):    
    if not visited[i]:
        bfs(i)
        link +=1
print(link)

'''
> result 
@ Memory : 65356 KB
@ Time : 884 ms
@ Code length : 593 B
'''