'''
> Problem
@ 백준 7576번
@ 토마토
@ URL https://www.acmicpc.net/problem/7576
'''

import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())

box=[]
matures=deque()
for i in range(M):
    row = list(map(int, input().split()))
    box.append(row)
    for j in range(N):
        if row[j] == 1:
            matures.append((i,j))
            
dx = [0, 0, -1, 1] # 상, 하, 좌, 우 
dy = [1, -1, 0, 0]

day = -1
while matures:
    day += 1
    
    for _ in range(len(matures)):
        tom_y, tom_x = matures.popleft()

        for i in range(4):
            next_x = tom_x + dx[i]
            next_y = tom_y + dy[i]
            
            if (0 <= next_x < N) and (0 <= next_y < M) and box[next_y][next_x] == 0:
                matures.append((next_y, next_x))
                box[next_y][next_x] = 1
                
for row in box:
    if 0 in row:
        day = -1
print(day)


'''
> result 
@ Memory : 98968 KB
@ Time : 2548 ms
@ Code length : 840 B
'''

