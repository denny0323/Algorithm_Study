'''
> Problem
@ 백준 Class4 1238번
@ 파티
@ URL https://www.acmicpc.net/problem/1238
'''

import heapq
import sys

input = sys.stdin.readline
inf = int(1e9)

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, T = map(int, input().split())
    graph[s].append((e, T))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    # heapq.heappush(q, (start, 0))
    
    distance = [inf] * (N + 1)
    distance[start] = 0
    
    while q:
        dist, node = heapq.heappop(q)
        # node, dist = heapq.heappop(q) : 시간 초과
        
        if distance[node] < dist: 
            continue
            
        for node_l, dist_l in graph[node]:
            cost = dist + dist_l
            
            if distance[node_l] > cost:
                distance[node_l] = cost 
                heapq.heappush(q, (cost, node_l))
                #heapq.heappush(q, (node_l, cost)) : 시간 초과
    return distance

r = 0
for i in range(1, N + 1):
    go = dijkstra(i)
    back = dijkstra(X)
    r = max(r, go[X] + back[i])
    
print(r)

'''
> result 
@ Memory : 31612 KB
@ Time : 2424 ms
@ Code length : 850 B
'''