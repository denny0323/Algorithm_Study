'''
> Problem
@ 백준 Class3 1764번
@ 듣보잡
@ URL https://www.acmicpc.net/problem/1764
'''

import sys

N, M = map(int, sys.stdin.readline().split())

nolistened = [sys.stdin.readline().strip() for _ in range(N)]
noseen = [sys.stdin.readline().strip() for _ in range(M)]

intersection = set(nolistened) & set(noseen)

print(len(intersection))
for i in sorted(intersection):
    print(i)
    
'''
> result
@ Memory : 42324 KB
@ Time : 128ms
@ Code length : 294B
'''
