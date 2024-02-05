'''
> Problem
@ 백준 문제집 <단기간 성장> 3197번
@ 백조의 호수
@ URL https://www.acmicpc.net/problem/3197
'''
### Sol1. day마다 얼음을 녹이고, 백조끼리 DFS로 최단 경로 찾기 --> 시간 초과
### Sol2. 물 BFS -> 빙판, 물 임시 큐 저장 -> 백조 BFS -> 빙판, 백조 임시큐 저장
###       -> 물, 백조 큐를 임시큐로 교체 -> 반복

# queue - 백조가 다른 백조를 찾을 때 사용하는 queue
# next_queue - 백조가 'X'를 만나면 추후에 물을 녹인 후 확인할 queue
# water - 물의 좌표를 담는 queue, 상하좌우에 X가 있는지 확인해야함
# next_water - 빙판을 녹여서 물로 만든 좌표를 다음 주기 때 다시 상하좌우에 'X'가 있는지 체크해야하므로, 그 정보를 담은 queue

import sys
input = sys.stdin.readline
from collections import deque

dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)


def find_swan(lake, visited, queue): # swan을 찾기
    next_queue = deque()
    
    while queue:
        r, c  = queue.popleft() # 이동된 백조의 위치가
        
        if r == swans[1][0] and c == swans[1][1]: # target swan인지 확인
            return True, None
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if not 0 <= nr < R or not 0 <= nc < C:
                continue
                
            if visited[nr][nc]:
                continue
                
            if lake[nr][nc] == 'X': # ices
                next_queue.append((nr, nc)) # 백조가 이동 가능한 범위의 ice라고 하면 다음날 녹여야할 것 -> 다음날 물이 됨 -> 다음날 백조가 갈 수 있음
                
            else:
                queue.append((nr, nc)) # 백조가 이동 가능한 위치를 모두 담음(하루에)
                
            visited[nr][nc] = True

    return False, next_queue


def melt_ice(waters, lake): # ice 인근의 물만 받아서 ice를 녹임
    next_waters = deque() # 현재의 ice가 녹은 것이 다음 날의 water
    
    while waters:
        r, c = waters.popleft() # BFS
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
        
            if not 0 <= nr < R or not 0 <= nc < C:
                continue
                
            if lake[nr][nc] == 'X': # ice를 만남
                next_waters.append((nr, nc)) # 다음날의 물 -> 다음 날의 ice 인근의 물
                lake[nr][nc] = '.' # 녹임
    
    return next_waters

R, C = map(int, input().split())

lake = []
swans = []
waters = deque() # water의 인근만 찾아본다


for r in range(R):
    row = list(input().strip())
    
    for c, v in enumerate(row):
        if v == '.' or v == 'L':
            waters.append((r, c)) # 물 좌표
        if v == 'L':
            swans.append((r, c))  # 백조 좌표
            
    lake.append(row)


day = 0
visited = [[False]*C for _ in range(R)]

queue = deque() # 백조를 찾는 과정
r, c = swans[0][0], swans[0][1]

queue.append((r, c))
visited[r][c] = True

while True:
    found, next_queue = find_swan(lake, visited, queue) # 백조가 이동가능한 위치를 모두 담고 그 중 다음 백조가 걸리나?
    if found: # 백조를 찾으면 멈추고 day를 return
        break 
    waters = melt_ice(waters, lake)
    queue = next_queue # 다음날의 백조 위치 (이동됨)
    day += 1
    
print(day)
'''
> result
@ Memory : 226776KB
@ Time : 7204ms
@ Code length : 397B
'''

