'''
> Problem
@ 백준 Class4 1504번
@ 특정한 최단 경로
@ URL https://www.acmicpc.net/problem/1504
'''


# * __다익스트라 알고리즘(Dijkstra)__
#     * 첫 정점을 기준으로 연결되어 있는 정점들을 추가해 가며 최단 거리를 갱신하는 기법
#     * 다익스트라 알고리즘은 BFS와 유사
#          * 첫 정점부터 각 노드 간의 거리를 저장하는 배열을 만든 후, 첫 정점의 인접 노드 간의 거리부터 먼저 계산하면서, 첫 정점부터 해당 노드 간의 가장 짧은 거리를 해당 배열에 업데이트
#     * 우선순위 큐를 활용 : 우선순위 큐는 Min Heap방식을 활용해서, 현재 가장 짧은 거리를 가진 노드 정보를 먼저 꺼내게 됨
#         * 첫 정점을 기준으로 배열을 선언하여 첫 정점에서 각 정점까지의 거리를 저장
#         * 초기에는 첫 정점의 거리는 0, 나머지는 무한대로 저장(inf)
#         * 우선순위 큐에 (첫 정점, 0)만 먼저 넣음
#     * 우선순위 큐에서 노드를 꺼냄
#         * 처음에는 첫 정점만 저장되어 있으므로, 첫 정점만 꺼내짐
#         * 첫 정점에 인접한 노드들 각각에 대해, 첫 정점에서 각 노드로 가는 거리와 현재 배열에 저장되어 있는 첫 정점에서 각 정점까지의 거리를 비교
#         * 배열에 저장되어 있는 거리보다, 첫 정점에서 해당 노드로 가는 거리가 더 짧을 경우 배열에 해당 노드의 거리를 업데이트
#         * 배열에 해당 노드의 거리가 업데이트된 경우, 우선순위 큐에 넣는다  
#         -> 결과적으로 너비 우선 탐색과 유사하게, 첫 정점에 인접한 노드들을 순차적으로 방문하게 됨  
#         -> 만약 배열에 기록된 현재까지 발견된 가장 짧은 거리보다 더 긴 거리를 가진 경우에 해당 노드와 인접한 노드 간의 거리 계산을 하지 않음
#     * 위 과정을 우선순위 큐에 꺼낼 노드가 없을 때까지 반복
#     
# __source : https://developer-wony.tistory.com/41__


import sys, heapq
input = sys.stdin.readline

def dijkstra(start, graph):
    dist = [float('inf')] * len(graph)
    dist[start] = 0
    
    heap = []
    heapq.heappush(heap, (start, 0))
    
    while heap:
        curr_node, curr_dist = heap.pop()
        
        if curr_dist > dist[curr_node]: # 시간단축
            continue
            
        for link_node, link_dist in graph[curr_node]:
            link_dist += dist[curr_node] # 현재 거쳐서의 거리로 비교
            if dist[link_node] > link_dist:
                dist[link_node] = link_dist 
                heapq.heappush(heap, (link_node, link_dist))
    return dist

N, E = map(int, input().split())
graph = [[] for i in range(N+1)]

for i in range(E):
    a, b, dist = map(int, input().split())
    graph[a].append((b,dist)); graph[b].append((a,dist));
v1, v2 = map(int, input().split())

dist_start = dijkstra(1, graph)
dist_v1 = dijkstra(v1, graph)
dist_v2 = dijkstra(v2, graph)

# start -> v1 -> v2 -> N or start -> v2 -> v1` -> N
d = min(dist_start[v1]+dist_v1[v2]+dist_v2[N], dist_start[v2]+dist_v2[v1]+dist_v1[N])
print(d if d != float('inf') else -1)


'''
> result 
@ Memory : 62568 KB
@ Time : 4500 ms
@ Code length : 1142 B
'''

