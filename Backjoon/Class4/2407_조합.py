'''
> Problem
@ 백준 Class4 2407번
@ 조합
@ URL https://www.acmicpc.net/problem/2407
'''

# import sys
# input = sys.stdin.readline
# input_file = open('./input/1991.txt', 'r')
# input = input_file.readline

Comb = [[0]*(i+1) for i in range(0,101)]
Comb[1][0] = 1; Comb[1][1] = 1

for i in range(2, 101):
    for j in range(i+1):
        if j == 0 or j == i:
            Comb[i][j] = 1
        elif j == 1:
            Comb[i][j] = i
        else:
            Comb[i][j] = Comb[i-1][j]+Comb[i-1][j-1]
            
n, m = map(int, input().split())
print(Comb[n][m])

'''
> result 
@ Memory : 28776 KB
@ Time : 64 ms
@ Code length : 343 B
'''