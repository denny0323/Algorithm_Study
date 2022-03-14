'''
> Problem
@ 백준 문제집 <단기간 성장> 1655번
@ 평범한 배낭
@ URL https://www.acmicpc.net/problem/1655
'''
# Sol 1. 
N = int(input())
baek = []

for _ in range(N):
    baek.append(int(input()))
    sorted_baek = sorted(baek)
    length = len(sorted_baek)
    
    if length % 2 == 0: print(min(sorted_baek[length//2-1], sorted_baek[length//2]))
    elif length == 1: print(sorted_baek[0])
    else: print(sorted_baek[int(length//2)])
    del sorted_baek, length
'''
> result : 시간초과
@ Code length : 397B
'''

# Sol 2.
import sys, heapq
input = sys.stdin.readline # 안했을 때 시간초과

N = int(input())
max_heap, min_heap = [], []

for _ in range(N):
    num = int(input())
    
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)
        
    if len(max_heap) >= 1 and len(min_heap) >= 1 and max_heap[0] * -1 > min_heap[0]:
        max_value = heapq.heappop(max_heap) * -1
        min_value = heapq.heappop(min_heap)
        
        heapq.heappush(max_heap, min_value * -1)
        heapq.heappush(min_heap, max_value)

    print(max_heap[0] * -1)
'''
> result : 
@ Memory : 36872KB
@ Time : 292ms
@ Code length : 591B
'''

