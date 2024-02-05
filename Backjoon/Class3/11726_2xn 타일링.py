'''
> Problem
@ 백준 Class3 11726번
@ 2xn 타일링
@ URL https://www.acmicpc.net/problem/11726
'''
############################## 시간초과 ##############################

import sys
sys.setrecursionlimit(10000)

N = int(input())

def Tiling(n):
    if n > 2:
        return Tiling(n-1) + Tiling(n-2)
    else: 
        return n

print(Tiling(N) % 10007)

'''
> result : 시간초과
'''


############################## 메모이제이션 도입 ##############################
'''
Python으로 이 문제를 풀 때 주의할 점 2가지.
1) 재귀 호출 범위 늘려주기
2) DP를 적용하고 메모이제이션을 꼭 적용해주어야 시간초과 회피 가능(★)
'''

import sys
sys.setrecursionlimit(10000)

N = int(input())
memory = [-1] * 1001 # 메모이제이션
 
def Tiling(n):
    if memory[n] != -1: return memory[n]
    if n in [1, 2]: return n
    memory[n] = (Tiling(n-1) + Tiling(n-2)) % 10007
    return memory[n]

print(Tiling(N))

'''
> result 
@ Memory : 29536 KB
@ Time : 80 ms
@ Code length : 277 B
'''