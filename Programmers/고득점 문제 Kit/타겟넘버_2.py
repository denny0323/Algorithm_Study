## BFS
# from collections import deque
# def solution(numbers, target):
#     answer = 0
#     queue = deque([(0, 0)])  # sum, level
#
#     while queue:
#         SUM, level = queue.popleft()
#         if level > len(numbers):
#             break
#         elif level == len(numbers) and sum == target:
#             answer += 1
#
#         queue.append((SUM + numbers[level - 1], level + 1))
#         queue.append((SUM - numbers[level - 1], level + 1))
#
#     return answer

numbers = [1, 1, 1, 1, 1]
target = 3

## DFS?
def solution(numbers, target):
    SUM = [0]
    for n in numbers:
        SUM_sub = []
        for m in SUM:
            SUM_sub.append(m + n)
            SUM_sub.append(m - n)
        SUM = SUM_sub
        # print(SUM_sub)
    return SUM.count(target)


##### DFS로 조합 구현
answer = 0
def DFS(idx, numbers, target, SUM):
    global answer
    N = len(numbers)
    if (idx == N and target == SUM):
        answer += 1
        return
    if idx == N:
        return

    DFS(idx+1,numbers,target,SUM+numbers[idx])
    DFS(idx+1,numbers,target,SUM-numbers[idx])

def solution(numbers, target):
    global answer
    DFS(0, numbers, target, 0)
    return answer


######### product의 기능

from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

