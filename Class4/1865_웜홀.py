'''
> Problem
@ 백준 Class4 1865번
@ 웜홀
@ URL https://www.acmicpc.net/problem/1865
'''

import sys
input = sys.stdin.readline

def Bellman_Ford():
    dist[1] = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            for time, node in road[j]:
                if dist[node] > time + dist[j]:
                    dist[node] = time + dist[j]
                    if i == N:
                        print('YES')
                        return
    print('NO')
    return

TC = int(input())
INF = float('inf')

for _ in range(TC):
    N, M, W = map(int, input().split())
    
    road = [[] for _ in range(N+1)] 
    dist = [1e9] * (N+1)
    
    for _ in range(M):
        S, E, T = map(int, input().split())
        road[S].append((T, E)); road[E].append((T, S))
    
    for _ in range(W):
        S, E, T = map(int, input().split())
        road[S].append((-T, E))
    
    Bellman_Ford()
    
'''
> result 
@ Memory : 29284 KB
@ Time : 1968 ms
@ Code length : 816 B
'''

