'''
> Problem
@ 백준 Class4 2096번
@ 내려가기
@ URL https://www.acmicpc.net/problem/2096
'''

# import sys
# input = sys.stdin.readline
# input_file = open('./input/1991.txt', 'r')
# input = input_file.readline

N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]    

def score():
    max_num = -1
    min_num = 1e6 
    for index in range(3):
        result = [0, 0]
        for n in range(N):
            if n == 0 :
                result[0] += field[n][index] # max
                result[1] += field[n][index] # min
            else:
                if index == 0:
                    result[0] += max(field[n][:2])
                    result[1] += min(field[n][:2])
                elif index == 1:
                    result[0] += max(field[n])
                    result[1] += min(field[n])
                else:
                    result[0] += max(field[n][1:])
                    result[1] += min(field[n][1:])
        if max_num < result[0]: max_num = result[0]
        if min_num > result[1]: min_num = result[1]
    print(max_num, min_num)
    
score()

'''
> result : 메모리 초과
'''

import sys, copy
input = sys.stdin.readline

N = int(input())

for n in range(N):
    line = list(map(int, input().split()))
                    
    if n == 0:
        dpMax = copy.deepcopy(line)
        dpMin = copy.deepcopy(line)
    else:
        tmpMax = copy.deepcopy(dpMax)
        tmpMin = copy.deepcopy(dpMin)
        
        for i in range(3):
            if i == 0:
                dpMax[i] = line[i] + max(tmpMax[:i+1])
                dpMin[i] = line[i] + min(tmpMin[:i+1])
            elif i == 1:
                dpMax[i] = line[i] + max(tmpMax)
                dpMin[i] = line[i] + min(tmpMin)
            else:
                dpMax[i] = line[i] + max(tmpMax[i-1:])
                dpMin[i] = line[i] + min(tmpMin[i-1:])
print(max(dpMax), min(dpMin))
'''
> result : 틀렸습니다.
'''

import sys, copy
input = sys.stdin.readline

N = int(input())

for n in range(N):
    line = list(map(int, input().split()))
                    
    if n == 0:
        dpMax = copy.deepcopy(line)
        dpMin = copy.deepcopy(line)
    else:
        tmpMax = copy.deepcopy(dpMax)
        tmpMin = copy.deepcopy(dpMin)
        
        for i in range(3):
            if i == 0:
                dpMax[i] = line[i] + max(tmpMax[i], tmpMax[i+1])
                dpMin[i] = line[i] + min(tmpMin[i], tmpMin[i+1])
            elif i == 1:
                dpMax[i] = line[i] + max(tmpMax[i-1], tmpMax[i], tmpMax[i+1])
                dpMin[i] = line[i] + min(tmpMin[i-1], tmpMin[i], tmpMin[i+1])
            else:
                dpMax[i] = line[i] + max(tmpMax[i-1], tmpMax[i])
                dpMin[i] = line[i] + min(tmpMin[i-1], tmpMin[i])
print(max(dpMax), min(dpMin))

'''
> result 
@ Memory : 29768 KB
@ Time : 1036 ms
@ Code length : 866 B
'''

import sys
input = sys.stdin.readline
 
N = int(input())
maxD = [[0 for _ in range(3)] for _ in range(2)] # 현재, 다음
minD = [[0 for _ in range(3)] for _ in range(2)] # 현재, 다음 

for n in range(N):
    temp = list(map(int, input().split()))
 
    maxD[1][0] = temp[0] + max(maxD[0][0], maxD[0][1]) 
    minD[1][0] = temp[0] + min(minD[0][0], minD[0][1]) 
 
    maxD[1][1] = temp[1] + max(maxD[0][0], maxD[0][1], maxD[0][2]) 
    minD[1][1] = temp[1] + min(minD[0][0], minD[0][1], minD[0][2]) 
 
    maxD[1][2] = temp[2] + max(maxD[0][1], maxD[0][2]) 
    minD[1][2] = temp[2] + min(minD[0][1], minD[0][2]) 
 
    maxD[0][0], maxD[0][1], maxD[0][2] = maxD[1][0], maxD[1][1], maxD[1][2]
    minD[0][0], minD[0][1], minD[0][2] = minD[1][0], minD[1][1], minD[1][2]

print(max(maxD[1]), min(minD[1]))

'''
> result 
@ Memory : 28776 KB
@ Time : 448 ms
@ Code length : 771 B
'''