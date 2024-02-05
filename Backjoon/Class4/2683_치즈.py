'''
> Problem
@ 백준 Class4 2683번
@ 치즈
@ URL https://www.acmicpc.net/problem/2683
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]
air = [[0]*M for _ in range(N)]

dx = [ 0, 0, -1, 1]
dy = [-1, 1,  0, 0]

# def check(cheese):
#     check = set()
#     for c in cheese:
#         check = check.union(set(c))
#     return check

def isMeltAll():
    for y in range(N):
        for x in range(M):
            if cheese[y][x] == 1:
                return False
    return True

# source: https://paris-in-the-rain.tistory.com/m/89?category=772932
# 이차원 리스트를 돌면서 4방탐색을 진행한다.
# 다음 진행 방향이 치즈면 큐에 넣는다
# 리스트의 범위를 초과하지 않아야 한다.
# 이미 큐에 넣은 좌표를 다시 넣지 않아야 한다.
# 큐에 들어간 좌표는 리스트에서 -1로 업데이트 한다.
# 이렇게 하면 내부 치즈와 맞닿은 공기들은 0으로 되어있고 외부 치즈와 맞닿은 공기만 -1로 된다.

def SetAir(cheese):
    visited = [[False]*M for _ in range(N)]
   
    q = []
    q.append((0, 0))
    
    air[0][0] = -1
    visited[0][0] = True
    
    while q:
        x, y = q.pop(0)
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if 0 <= new_x < M and 0 <= new_y < N:
                if cheese[new_y][new_x] == 0 and not visited[new_y][new_x]:
                    q.append((new_x, new_y))
                    air[new_y][new_x] = -1
                    visited[new_y][new_x] = True
    return

time = 0
while not isMeltAll():
    SetAir(cheese)
    tmp = [] # 좌표저장 후 한번에 녹여야함
    for y in range(1,N):
        for x in range(1,M):

            if cheese[y][x] == 1:
                cnt = 0
                for r in range(4):
                    new_x, new_y = x + dx[r], y + dy[r]
                    
                    if air[new_y][new_x] == -1:
                        cnt += 1
                    
                if cnt >= 2:
                    tmp.append((x, y))
    for x, y in tmp:
        cheese[y][x] = 0
        
    #for c in cheese:
    #    print(*c)
    #print('\n')

    time += 1

print(time)
'''
> result 
@ Memory : 28776 KB
@ Time : 1668 ms
@ Code length : 1433 B
'''

