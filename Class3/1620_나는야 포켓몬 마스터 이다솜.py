'''
> Problem
@ 백준 Class3 1620번
@ 나는야 포켓몬 마스터 이다솜
@ URL https://www.acmicpc.net/problem/1620
'''

import sys
N, M = map(int, sys.stdin.readline().split())

Poketmons = []
Pokedex = {}
for i in range(1,N+1):
    poketmon = sys.stdin.readline().rstrip()
    Pokedex[poketmon] = i
    Poketmons.append(poketmon)
    
for _ in range(M):
    Q = sys.stdin.readline().rstrip()
    try: 
        Q = int(Q)
        print(Poketmons[Q-1])
    except:
        print(Pokedex[Q])   

'''
> result
@ Memory : 46916 KB
@ Time : 320ms
@ Code length : 372B
'''
