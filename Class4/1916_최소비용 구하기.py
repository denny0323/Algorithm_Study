'''
> Problem
@ 백준 Class4 1916번
@ 최소비용 구하기
@ URL https://www.acmicpc.net/problem/1916
'''
import sys, heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
inf = float('inf')
graph = [[] for _ in range(N+1)] 

for _ in range(M):
    s, e, cost = map(int, input().split())
    graph[s].append((cost, e)) 
    
Start, End = map(int, input().split())

def Dijstra(start):
    dist = [inf] * (N+1)  # 두 도시간의 비용이 1e5인 것. 1e5보다 훨씬 큰 수로 해야함. 1e5로 초기화해서 틀림
    dist[start] = 0
    
    heap = []
    heapq.heappush(heap, (0, start))
    
    while heap:
        curr_cost, curr_node = heapq.heappop(heap)
        
        if curr_cost > dist[curr_node]:
            continue
        
        for cost_pop, node_pop in graph[curr_node]:
            cost_pop += dist[curr_node]
            if cost_pop < dist[node_pop]:
                dist[node_pop] = cost_pop
                heapq.heappush(heap, (cost_pop, node_pop))
    return dist

print(Dijstra(Start)[End])

'''
> result 
@ Memory : 42620 KB
@ Time : 276 ms
@ Code length : 823 B
'''