'''
> Problem
@ 백준 Class3 1012번
@ 유기농 배추
@ URL https://www.acmicpc.net/problem/1012
'''
#### DFS ####

import sys

# input_file = open('1012_2.txt', 'r')
def DFS(field, r, c):
    dr = [0, 1, 0, -1]  # Right, Up, Left, Down
    dc = [1, 0, -1, 0]
    temp = [[r, c]]

    while temp:
        r, c = temp.pop()
        field[r][c] = -1
        for i in range(4):
            r_new = r + dr[i]
            c_new = c + dc[i]
            if 0 <= r_new < N and 0 <= c_new < M and field[r_new][c_new] == 1:
                temp.append([r_new, c_new])


# T = int(input_file.readline())
T = int(input())
for _ in range(T):
    # M, N, K = map(int, input_file.readline().split())
    M, N, K = map(int, sys.stdin.readline().split())

    # 밭 형성
    field = [[0] * M for i in range(N)]
    for _ in range(K):
        # c, r = map(int, input_file.readline().split())
        c, r = map(int, sys.stdin.readline().split())

        field[r][c] = 1

    # 지렁이 초기화
    warm = 0

    # 탐색(DFS)
    for n in range(N):
        for m in range(M):
            if field[n][m] <= 0:
                field[n][m] = -1
            else:
                warm += 1
                DFS(field, n, m)
    print(warm)


'''
> result
@ Memory : 29028KB
@ Time : 84ms
@ Code_length : 1116B
'''

#### BFS ####

import sys
from collections import deque

# input_file = open('1012_1.txt', 'r')
def BFS(field, r, c):
    dr = [0, 1, 0, -1]  # Right, Up, Left, Down
    dc = [1, 0, -1, 0]
    temp = deque([(r, c)])

    while temp:
        r, c = temp.popleft()
        field[r][c] = -1
        for i in range(4):
            r_new = r + dr[i]
            c_new = c + dc[i]
            if 0 <= r_new < N and 0 <= c_new < M and field[r_new][c_new] == 1:
                field[r_new][c_new] = -1
                temp.append([r_new, c_new])


# T = int(input_file.readline())
T = int(input())
for _ in range(T):
    # M, N, K = map(int, input_file.readline().split())
    M, N, K = map(int, sys.stdin.readline().split())

    # 밭 형성
    field = [[0] * M for i in range(N)]
    for _ in range(K):
        # c, r = map(int, input_file.readline().split())
        c, r = map(int, sys.stdin.readline().split())

        field[r][c] = 1

    # 지렁이 초기화
    warm = 0

    # 탐색(DFS)
    for n in range(N):
        for m in range(M):
            if field[n][m] <= 0:
                field[n][m] = -1
            else:
                warm += 1
                BFS(field, n, m)
    print(warm)

'''
> result
@ Memory : 32052KB
@ Time : 100ms
@ Code_length : 1197B
'''
