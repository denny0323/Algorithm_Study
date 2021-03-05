  
'''
> Problem
@ 백준 Class3 1463번
@ URL https://www.acmicpc.net/problem/1463
'''


# (핵심 아이디어)
# 점화식
# dp[N] = min(dp[N-1], dp[N//2] , dp[N//3]) + 1 

N = int(input())
dp = [0,0,1,1] # 0 ,1, 2, 3 의 최소 수 미리 저장

for i in range(4, N + 1) :
    dp.append(dp[i-1] + 1)

    if i % 2 == 0 :
        dp[i] = min(dp[i], dp[i//2] + 1) 

    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i//3] + 1) 

print(dp[N])

'''
> result
@ Memory : 37024 KB
@ Time : 632 ms
@ Code length : 276 B
'''