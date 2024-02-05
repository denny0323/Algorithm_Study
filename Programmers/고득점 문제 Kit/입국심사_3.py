def solution(n, times):
    answer = 0

    left, right = min(times), max(times) * n
    while left <= right:
        mid = (left + right) // 2   ## checking time
        PASS = 0

        for time in times:          ## 현재 time(mid)를 기준으로 각 심사관마다 몇 명이나 pass했는지
            PASS += mid // time

            if PASS >= n:           ## 더하다가 기준 인원을 넘으면 break
                break

        if PASS >= n:  ## 이미 넘었다면, mid가 충분함 -> 시간을 줄여도 됨
            answer = mid
            right = mid - 1

        elif PASS < n: ## 아직 받아야할 사람이 남았으면 mid를 늘려야함
            left = mid + 1

    return answer
