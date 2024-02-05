m = 4; n = 3
puddles = [[2, 2]]


########### 내 풀이 ############
map = [[0]*m for _ in range(n)]
map[0][0] = 1
for j in range(n):
    for i in range(m):
        # print('현재 state', j, i)
        if [i+1, j+1] in puddles:
            continue
        else:
            for dx, dy in [(-1, 0), (0, -1)]: # 왼쪽 cell, 위쪽 cell
                if 0<= i+dx < m and 0<= j+dy < n: # 현재 위치의 왼쪽 위치가 유효하다면,
                    # print(j+dy, i+dx)
                    # print('현재 cell', map[j][i])
                    # print('참조 cell', map[j+dy][i+dx])
                    map[j][i] += map[j+dy][i+dx]
                    # print('결과', map[j][i])
print(map[n-1][m-1] % 1000000007)


########### 더 좋은 풀이? ############
map = [[0] * (m+1) for _ in range(n+1)]
map[1][1] = 1

for i in range(1, n+1):
    for j in range(1, m+1):
        if [j, i] in puddles or [i, j] == [1, 1]:
            continue
        else:
            map[i][j] = map[i-1][j] + map[i][j-1]

print(map[-1][-1] % 1000000007)


