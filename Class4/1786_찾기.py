'''
> Problem
@ 백준 Class4 1786번
@ 찾기
@ URL https://www.acmicpc.net/problem/1786
'''
T = input()
P = input()

def pi(P):
    len_p = len(P)
    pi = [0]*len_p
    
    j = 0
    for i in range(1, len_p):
        while j > 0 and P[i] != P[j]:
            j = pi[j-1]
            
        if P[i] == P[j]:
            j += 1
            pi[i] = j
    
    return pi            

Is = []
Pi = pi(P); p = len(P); t = len(T)
j = 0

for i in range(t):
    while j > 0 and T[i] != P[j]:
        j = Pi[j-1]
            
    if T[i] == P[j]:
        if j == p-1:
            Is.append(i-p+2)
            j = Pi[j]
        else:
            j += 1
            
print(len(Is))
print(*Is)
'''
> result 
@ Memory : 76200 KB
@ Time : 868 ms
@ Code length : 592 B
'''