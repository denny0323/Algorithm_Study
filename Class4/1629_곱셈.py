'''
> Problem
@ 백준 Class4 1629번
@ 곱셈
@ URL https://www.acmicpc.net/problem/1629
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def power(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x*power(x,n-1)

A, B, C = map(int, input().split())
print(power(A, B)%C)

'''
> result : 런타임 에러 (RecursionError)
'''

import sys
input = sys.stdin.readline

def power(x, n):
    if n == 1:
        return x % C
    else:
        tmp = power(x, n//2)
        if n % 2 == 0:
            return (tmp * tmp) % C
        else:
            return (tmp * tmp * x) % C

A, B, C = map(int, input().split())
print(power(A, B))

'''
> result 
@ Memory : 28776 KB
@ Time : 68 ms
@ Code length : 297 B
'''