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


# 곱셈의 개수를 줄이는 "분할 정복"이 필요
#  
# 1. b의 값이 짝수인지 홀수인지 파악한다.
# 2. b의 값이 짝수라면 10 ^10 -> (10^5)^2 형태로 바꿔준다.
# 3. b의 값이 홀수라면 10 ^11 -> (10^5)^2 * 10 형태로 바꿔준다.
# -> `B`를 2에 대한 거듭제곱 형태로 계속하여 분할하여 `B`만큼 `A`를 거듭제곱 하는 것이 아니라 
#    제곱을 한 뒤, 거기에 제곱을 또하고 또 하는 방식을 취하여 연산 수를 최대한 줄여볼 것
#     e.g. A^50 = (A^25)^2 = ((A^12)^2 * A)^2


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
