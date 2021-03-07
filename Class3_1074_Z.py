'''
> Problem
@ 백준 Class3 1074번
@ Z
@ URL https://www.acmicpc.net/problem/1074
'''


N,r,c = map(int, input().split())
num = 0

quadrant=[(0, 0), (0, 1), (1, 0), (1, 1)]

while N > 0:
    if N == 1:
        num += quadrant.index((r,c))
        break
    elif N > 1:
        std = 2**(N-1)
        new_r, new_c = r//std, c//std
        if new_r == 1 and new_c == 1:
            num += 3*(std**2)

        elif new_r == 1 and new_c == 0:
            num += 2*(std**2)

        elif new_r == 0 and new_c == 1:
            num += 1*(std**2)
        else:
            num += 0

    r -= std*new_r
    c -= std*new_c 
    N -= 1
print(num)

'''
> result
@ Memory : 28776 KB
@ Time : 72ms
@ Code_length : 548B
'''

