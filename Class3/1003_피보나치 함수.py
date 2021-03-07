  
'''
> Problem
@ 백준 Class3 1003번
@ 피보나치 함수
@ URL https://www.acmicpc.net/problem/1003
'''

import sys
T = int(input())

zeros = [1,0]
ones = [0,1]

for i in range(2,41):
    zeros.append(zeros[i-1]+zeros[i-2])
    ones.append(ones[i-1]+ones[i-2])

for _ in range(T):
    n = int(input())
    print(zeros[n], ones[n])

'''
result
@ Memory : 28776 KB
@ Time : 72ms
@ Code length : 226B
'''
