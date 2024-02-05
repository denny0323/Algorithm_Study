'''
> Problem
@ 백준 Class4 1167번
@ 트리의 지름
@ URL https://www.acmicpc.net/problem/1167
'''

import sys
from collections import deque
input = sys.stdin.readline

def dist(i, tree):
    dists = [-1]*(V+1)
    q = deque()
    dist = 0
    q.append(i)
    dists[i] = dist
    
    while q:
        curr = q.pop()
        for link_node, link_dist in tree[curr]:
            if dists[link_node] == -1:
                dists[link_node] = dist + link_dist
                q.append(link_node)
        dist += link_dist
        
    return dists[i:]

V = int(input())
tree = {i:[] for i in range(1, V+1)}
for _ in range(V):
    info = list(map(int, input().split()))
    start = 1
    while info[start] != -1:
        tree[info[0]].append((info[start], info[start+1]))
        start += 2
        
rad = -1
for i in range(1, V):
    if rad < max(dist(i, tree)):
        rad = max(dist(i, tree))
print(rad)

'''
> result : 시간초과
> "트리의 지름은 임의의 하나의 노드 A에서 가장 거리가 먼 노드 B를 구하고, 
이 노드 B에서 가장 거리가 먼 노드 C를 구하게 되었을 때, B와 C 사이의 거리
'''

import sys
from collections import deque
input = sys.stdin.readline

def dist(i):
    dists = [-1]*(V+1)
    q = deque()
    q.append(i)
    dists[i] = 0
    max_dist = [0, 0]
    
    while q:
        curr = q.pop()
        for link_node, link_dist in tree[curr]:
            if dists[link_node] == -1:
                dists[link_node] = dists[curr] + link_dist
                q.append(link_node)
                if max_dist[1] < dists[link_node]:
                    max_dist = [link_node, dists[link_node]]
        
    return max_dist

V = int(input())
tree = {i:[] for i in range(1, V+1)}
for _ in range(V):
    info = list(map(int, input().split()))
    start = 1
    while info[start] != -1:
        tree[info[0]].append((info[start], info[start+1]))
        start += 2
        
max_node, max_dist = dist(1)
max_node, max_dist = dist(max_node)
print(max_dist)

'''
> result 
@ Memory : 80464 KB
@ Time : 836 ms
@ Code length : 867 B
'''