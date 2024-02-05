def solution(N, number):
    if N == number:
        return 1

    result = [set([int(str(N) * i)]) for i in range(1, 9)]
    for i in range(2, 9):  # N을 i번 사용했을 때
        for j in range(1, i):  # N을 1~i번까지 사용한 결과들마다
            for num_former in result[j - 1]:  # N을 j번 사용한 결과에 대해
                for num_latter in result[i - j - 1]:
                    result[i - 1].add(num_former + num_latter)
                    result[i - 1].add(num_former - num_latter)
                    result[i - 1].add(num_former * num_latter)
                    if num_latter > 0:
                        result[i - 1].add(num_former // num_latter)
        if number in result[i - 1]:
            return i
    return -1


N = 2; number = 11
print(solution(N, number))