'''
> Problem
@ 백준 Class3 11399번
@ ATM
@ URL https://www.acmicpc.net/problem/11399
'''

import sys
input = sys.stdin.readline
N = int(input())
line = list(map(int, input().split()))

line.sort()
time = 0
for i in range(N):
    time += sum(line[:i+1])
    
print(time)
    
'''
> result 
@ Memory : 28776 KB
@ Time : 72 ms
@ Code length : 179 B
'''