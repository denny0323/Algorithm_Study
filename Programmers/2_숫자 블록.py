def getMyDivisor(n):
    divisorsList = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if (n % i == 0):
            divisorsList.append(i)
            if ((i ** 2) != n):
                divisorsList.append(n // i)
    divisorsList.sort()
    return divisorsList


def solution(begin, end):
    answer = []
    for x in range(begin, end + 1):
        divisors = getMyDivisor(x)

        if len(divisors) == 1:  ## 1 일때는 0
            answer.append(0)

        elif len(divisors) == 2:
            answer.append(1)

        elif (x // divisors[1]) >= 10**7:
            answer.append(0)

        else:
            answer.append(x // divisors[1])

    return answer

