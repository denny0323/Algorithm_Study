'''
> Problem
@ 백준 Class3 7662번
@ 이중 우선순위 큐
@ URL https://www.acmicpc.net/problem/7662
'''

import sys, heapq

def sync(q):
    while q and visited[q[0][1]] == 0:
        heapq.heappop(q)
        
input = sys.stdin.readline
T = int(input())
visited = [0]*1000000

for _ in range(T):
    k = int(input())
    min_heap, max_heap = [], []
    
    for i in range(k):
        oper, num = input().strip().split()
        num = int(num)
        
        if oper == 'I':
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            visited[i] = 1
        else:
            if num == 1:
                sync(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = 0
                    heapq.heappop(max_heap)
            else:
                sync(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = 0
                    heapq.heappop(min_heap)
    sync(max_heap)
    sync(min_heap)
    
    if max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
    
'''
> result 
@ Memory : 160528 KB
@ Time : 8256 ms
@ Code length : 994 B
'''