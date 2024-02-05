'''
> Problem
@ 백준 Class4 9251번
@ LCS
@ URL https://www.acmicpc.net/problem/9251
'''


# ### Dynamic Programming
# * source1: https://suri78.tistory.com/11
# * source2: https://velog.io/@piopiop/%EB%B0%B1%EC%A4%80-9251-LCS-%ED%8C%8C%EC%9D%B4%EC%8D%AC


import sys
#sys.stdin = open('./input/9251.txt', 'r')
input = sys.stdin.readline

string1 = input().rstrip()
string2 = input().rstrip()

LCS = [[0] * (len(string1)+1) for _ in range(len(string2)+1)]

for i in range(1, len(string1)+1): 
    for j in range(1, len(string2)+1): 
        if string1[i-1] == string2[j-1]: 
            LCS[i][j] = LCS[i-1][j-1] + 1 
        else: 
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1]) 

print(LCS[-1][-1])

'''
> result 
@ Memory : 36224 KB
@ Time : 708 ms
@ Code length : 420 B
'''

