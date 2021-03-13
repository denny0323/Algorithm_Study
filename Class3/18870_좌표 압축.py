'''
> Problem
@ 백준 Class3 18870번
@ 좌표 압축
@ URL https://www.acmicpc.net/problem/18870
'''

############################## BEST ##############################

import sys
input = sys.stdin.readline
N = int(input())
coords = list(map(int, input().split())) 
sorted_coords = sorted(coords)
compress = {}

key = 0
for i in range(N):
    if sorted_coords[i] not in compress.keys():
        compress[sorted_coords[i]] = key
        key += 1
        
for i in coords:
    print(compress[i], end=' ')
    
'''
> result 
@ Memory : 154448 KB
@ Time : 2148 ms
@ Code length : 334 B
'''
    
    
############################## print 다르게 시도 : 메모리, 시간 늘어남 #############################

import sys
input = sys.stdin.readline
N = int(input())
coords = list(map(int, input().split())) 
sorted_coords = sorted(coords)
compress = {}

key = 0
for i in range(N):
    if sorted_coords[i] not in compress.keys():
        compress[sorted_coords[i]] = key
        key += 1

result = []                         ### 메모리, 시간 늘어남
for i in coords:
    result.append(str(compress[i]))
print(' '.join(result))

'''
> result 
@ Memory : 202832 KB
@ Time : 2256 ms
@ Code length : 374 B
'''

############################## set으로 tie값 처리 #############################

import sys
input = sys.stdin.readline
N = int(input())
coords = list(map(int, input().split())) 
tie_coords = sorted(list(set(coords)))   ### 메모리는 절약, 시간 더 늘어남
compress = {}
for i in range(len(tie_coords)):
    compress[tie_coords[i]] = i
        
for i in coords:
    print(compress[i], end=' ')

'''
> result 
@ Memory : 154448 KB
@ Time : 2396 ms
@ Code length : 272 B
'''

############################## set으로 tie값 처리(메모리절약ver) #############################

import sys
input = sys.stdin.readline
N = int(input())
coords = list(map(int, input().split())) 
tie_coords = list(set(coords))              #### 시간만 조금 늘어남 (140ms)
tie_coords.sort()
compress = {}
for i in range(len(tie_coords)):
    compress[tie_coords[i]] = i
        
for i in coords:
    print(compress[i], end=' ')
    
'''
> result 
@ Memory : 154448 KB
@ Time : 2288 ms
@ Code length : 282 B
'''