'''
> Problem
@ 백준 Class3 1697번
@ 숨바꼭질
@ URL https://www.acmicpc.net/problem/1697
'''
import sys
from collections import deque

#input_file = open('1697.txt', 'r')
#Start, End = map(int, input_file.readline().split())

Start, End = map(int, sys.stdin.readline().split())

MAX = 10**5+1
dist = [0]*MAX

q = deque()
q.append(Start)

while q:
    curr = q.popleft()
    if curr == End:
        print(dist[curr])
        break
    for child in (curr-1, curr+1, 2*curr):
        if 0<=child<MAX and not dist[child]:
            dist[child] = dist[curr] + 1
            q.append(child)
#     print(q)

'''
> result
@ Memory : 35492KB
@ Time : 192ms
@ Code_length : 508B
'''
