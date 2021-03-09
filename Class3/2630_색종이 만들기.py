'''
> Problem
@ 백준 Class3 2630번
@ 색종이 만들기
@ URL https://www.acmicpc.net/problem/2630
'''

import sys
input = sys.stdin.readline
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

def check_align(paper, summ=0):
    check = len(paper)**2
    for i in paper:
        summ += sum(i)
    align = False if 0 < summ < check else True
    color = 1 if summ == check else summ
    return align, color
    
def slicing(N, paper):
    # 사분면 자르기
    Q1=[];Q2=[];Q3=[];Q4=[]
    for i in range(0, N//2):
        Q1.append(paper[i][:N//2])
        Q2.append(paper[i][N//2:])
    for j in range(N//2, N):
        Q3.append(paper[j][:N//2])
        Q4.append(paper[j][N//2:])
    return [Q1, Q2, Q3, Q4]
    
cut = []
cut.append(paper)

W=0; B=0
while cut:
    tocut = cut.pop(0)
    align, color = check_align(tocut)
    if align:
        if color == 0:
            W += 1
        else:
            B += 1
    else:
        cutout = slicing(len(tocut), tocut)
        cut += cutout
print(W)
print(B)
    
'''
> result 
@ Memory : 31588 KB
@ Time : 152 ms
@ Code length : 934 B
'''