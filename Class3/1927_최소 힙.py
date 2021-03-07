'''
> Problem
@ 백준 Class3 1927번
@ 최소 힙
@ URL https://www.acmicpc.net/problem/1927
'''
import sys, heapq 

N = int(sys.stdin.readline())

heap = []
for i in range(N):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(heap, x)
    else:
        if len(heap) == 0 :
            print(0)
        else:
            curr_min = heapq.heappop(heap)
            print(curr_min)
'''
> result
@ Memory : 34700 KB
@ Time : 172ms
@ Code length : 303B
'''
