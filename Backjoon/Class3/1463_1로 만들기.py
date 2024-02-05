  
'''
> Problem
@ 백준 Class3 1463번
@ 1로 만들기
@ URL https://www.acmicpc.net/problem/1463
'''


# (핵심 아이디어)
# 점화식
# dp[N] = min(dp[N-1], dp[N//2] , dp[N//3]) + 1 

N = int(input())
# dp = [0, 0, 1, 1]
dp = [0]*(N+1)

# for i in range(4, N + 1):
#    dp.append(dp[i-1] + 1)

for i in range(2, N + 1) :
    dp[i] = dp[i-1] + 1

    if i % 2 == 0 :
        dp[i] = min(dp[i], dp[i//2] + 1) 

    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i//3] + 1) 

print(dp[N])

'''
> result
@ Memory : 37024 KB -> 36588 KB
@ Time : 632 ms -> 648 ms
@ Code length : 276 B -> 238 B
'''
