'''
> Problem
@ 백준 Class3 1931번
@ 회의실 배정
@ URL https://www.acmicpc.net/problem/1931
'''

############################## 1 ##############################
import sys
input = sys.stdin.readline
N = int(input())

scheduler = []
for _ in range(N):
    start, end = map(int, input().split())
    scheduler.append((start, end))
       
scheduler.sort(key=lambda x: x[1])

result = []
result.append(scheduler[0])
for i in range(1, N):
    if scheduler[i][0] >= result[-1][1]:
        result.append(scheduler[i])

print(len(result))

'''
> result : 틀렸습니다.
why? (반례) 종료시간만 같을 경우, 시작시간을 고려하지 않는다면, 
정렬에 따라 답이 2가지가 나올 수 있음

ex. [(2,2), (1,2), (1,4), (3,4), (3,5)] -> result : 2
ex. [(1,2), (2,2), (1,4), (3,4), (3,5)] -> result : 3

> solution : 시작시간에 대해서도 정렬
'''

############################## 2 ##############################
import sys
input = sys.stdin.readline
N = int(input())

scheduler = []
for _ in range(N):
    start, end = map(int, input().split())
    scheduler.append((start, end))
    
scheduler.sort(key=lambda x: x[0])    
scheduler.sort(key=lambda x: x[1])

result = []
result.append(scheduler[0])
for i in range(1, N):
    if scheduler[i][0] >= result[-1][1]:
        result.append(scheduler[i])

print(len(result))

'''
> result
@ Memory : 43664 KB
@ Time : 344 ms
@ Code length : 406 B
'''