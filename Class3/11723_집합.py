'''
> Problem
@ 백준 Class3 11723번
@ 집합
@ URL https://www.acmicpc.net/problem/11723
'''

import sys
input = sys.stdin.readline
M = int(input())

Set = [-1]*20

for i in range(M):
    inputs = list(input().strip().split())
    if len(inputs) > 1:
        oper, num = inputs 
        num = int(num)
    else: 
        oper = inputs[0] 
    
    if oper == 'add' and Set[num-1] == -1:
        Set[num-1] = num
        
    elif oper == 'remove' and Set[num-1] == num:
        Set[num-1] = -1
        
    elif oper == 'check':
        result = 1 if Set[num-1] == num else 0
        print(result)
        
    elif oper == 'toggle': 
        if Set[num-1] == num:
            Set[num-1] = -1
        else:
            Set[num-1] = num
            
    elif oper == 'all':
        Set = [i+1 for i in range(20)]
    
    else:
        Set = [-1]*20    
        
    
'''
> result 
@ Memory : 29028 KB
@ Time : 5556 ms
@ Code length : 762 B
'''