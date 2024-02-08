arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
def solution(arr1, arr2):
    M = len(arr1);
    N = len(arr2[0])
    answer = [[0] * N for _ in range(M)]

    for i in range(M):
        for j in range(N):
            col_arr2 = [row2[j] for row2 in range(arr2)]

            answer[i][j] = sum([r * c for r, c in zip(arr1[i], col_arr2)])

    return answer

solution(arr1, arr2)