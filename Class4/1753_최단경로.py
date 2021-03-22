'''
> Problem
@ 백준 Class4 1753번
@ 최단 경로
@ URL https://www.acmicpc.net/problem/1753
'''

import sys, heapq

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def Dijkstra(i):
    distance = [float('INF')] * (V + 1)
    distance[i] = 0

    heap = []
    heapq.heappush(heap, (0, i))

    while heap:
        dist, node = heapq.heappop(heap)

        if dist > distance[node]:
            continue

        for l_n, l_w in graph[node]:
            l_w += distance[node]
            if distance[l_n] > l_w:
                distance[l_n] = l_w
                heapq.heappush(heap, (l_w, l_n))
    return distance


result = Dijkstra(K)
for i in result[1:]:
    if i == float('inf'):
        print('INF')
    else:
        print(i)

'''
> result 
@ Memory : 65952 KB
@ Time : 764 ms
@ Code length : 819 B
'''

