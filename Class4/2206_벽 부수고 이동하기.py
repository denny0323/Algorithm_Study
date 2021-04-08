'''
> Problem
@ 백준 Class4 2206번
@ 벽 부수고 이동하기
@ URL https://www.acmicpc.net/problem/2206
'''
import sys
input = sys.stdin.readline

def bfs():
    dx = [ 0, 0, -1, 1] # 상, 하, 좌, 우
    dy = [-1, 1,  0, 0]
    
    q = []
    dist[0][0][0] = 1 # 시작점도 경로에 포함
    q.append((0, 0, False))  # (x, y, Break?)
    
    while q:
        x, y, Break = q.pop(0)
        curr_dist = dist[y][x][Break]        
        
        for i in range(4): # for 내에선 Break 변수가 일관되어야함.
            next_x = x + dx[i]
            next_y = y + dy[i]
            
            if next_x < 0 or next_x >= M or next_y < 0 or next_y >= N:
                continue
            
            if Map[next_y][next_x] and not Break and not dist[next_y][next_x][Break]: # 다음 찾을 게 벽이냐? Yes. 안 뚫어봄
                dist[next_y][next_x][1] += curr_dist+1 # 뚫은거에 저장
                q.append((next_x, next_y, True))
                
            elif not Map[next_y][next_x] and not dist[next_y][next_x][Break]: # 벽 아님, 안가봄
                dist[next_y][next_x][Break] = curr_dist+1
                q.append((next_x, next_y, Break))
                        
    print(dist[N-1][M-1][Break] if dist[N-1][M-1][Break] else -1)    

N, M = map(int, input().split())
Map = [list(map(int, input().rstrip())) for _ in range(N)]
dist = [[[0, 0] for _ in range(M)] for _ in range(N)]

bfs()
    
'''
> result 
@ Memory : 172,112 KB
@ Time : 5584 ms
@ Code length : 1339 B (주석포함 1320 B)
'''