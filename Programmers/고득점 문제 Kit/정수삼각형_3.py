triangle = [[7], [3,8], [8,1,0], [2,7,4,4], [4,5,2,6,5]]
dp = [[0]*n for n in range(1, len(triangle)+1)]

dp[0][0] = triangle[0][0]
for i in range(1, len(dp)):
    for j in range(i+1):
        if j == 0:  # 가장 처음 cell
            dp[i][j] = triangle[i][j] + dp[i-1][j]
        elif j == i: # 가장 마지막 cell
            dp[i][j] = triangle[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])
        print('i, j', (i, j), triangle[i][j], dp[i][j])
print(dp)