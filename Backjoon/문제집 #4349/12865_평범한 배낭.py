'''
> Problem
@ 백준 문제집 <단기간 성장> 12865번
@ 평범한 배낭
@ URL https://www.acmicpc.net/problem/12865
'''
import sys

N, K = map(int, sys.stdin.readline().split())

bag = [[0, 0]]
for _ in range(N):
    bag.append(list(map(int, sys.stdin.readline().split())))

d = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, K + 1):
        W, V = bag[i][0], bag[i][1]

        if j < W:
            d[i][j] = d[i - 1][j]
        else:
            d[i][j] = max(d[i - 1][j], d[i - 1][j - W] + V)
print(d[N][K])
'''
> result
@ Memory : 226776KB
@ Time : 7204ms
@ Code length : 397B
'''
