n = 3
left = 2
right = 5
#
# from itertools import chain
# def solution(n, left, right):
#     answer = []
#     matrix = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if matrix[i][j] == 0:
#                 matrix[i][j] = max(i, j) + 1
#     arr = [matrix[i] for i in range(n)]
#     arr = list(chain(*arr))
#     print(arr)
#
# solution(n, left, right)

'''
    6 / 20
    정확성 : 30.0 / 100.0
    (시간초과)
'''


def solution(n, left, right):
    coords = [(k // n, k % n) for k in range(left, right + 1)]
    print(coords)

    min_r = min([x[0] for x in coords])
    max_r = max([x[0] for x in coords])
    rows = {}
    for r in range(min_r, max_r+1):
        rows[r] = [0] * n
        for j in range(n):
            if j < r+1:
                rows[r][j] = r+1
            else:
                rows[r][j] = j+1
    print(rows)

    arr = [rows[i][j] for i, j in coords]
    print(arr)
    return arr

solution(n, left, right)
'''
    20 / 20
'''

def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)
    return answer
