# people = [70, 50, 80]
# limit = 200

# def solution(people, limit):
#     n = len(people)
#     pairs = []
#     IsPaired = [False] * n
#     for i, person in enumerate(people):
#         boat = [person]
#         room = limit - person
#         # print(IsPaired[i])
#         if IsPaired[i]:
#             continue
#
#         for j in range(i + 1, n):
#             if room >= people[j] and len(boat) < 2:
#                 boat.append(people[j])
#                 room -= people[j]
#                 IsPaired[j] = True
#
#             if len(boat) == 2:
#                 break
#
#         pairs.append(len(boat))
#         IsPaired[i] = True
#         # print(boat, IsPaired)
#     # print(pairs)
#     return len(pairs)

### 정확성 : 20.0
### 효율성 : 0.0

people = [70, 50, 80, 50]
limit = 100
answer = 0

## Two pointer
def solution(people, limit):
    people.sort()    ## people을 정렬하고
    answer = 0
    first = 0; last = len(people)-1  ## 가장 큰 몸무게와 가장 작은 몸무게의 합을 limit과 비교

    while first <= last:
        if people[first] + people[last] <= limit:  ## limit 이내라면 둘다 태우고 (first, last를 각각 늘리고 좁힘)
            first += 1
        last -= 1            ## 아니라면, 가장 큰 몸무게만 태움 (last만 줄임, if문 생략)
        answer += 1          ## 확인하면 무조건 태우는 경우는 수를 counting함 (2 or 1)

    return answer


## Two pointer
from collections import deque
def solution(people, limit):
    result = 0
    deque_people = deque(sorted(people))

    while deque_people:
        left = deque_people.popleft()
        if not deque_people: # 비었음
            return result + 1
        right = deque_people.pop()
        if left + right > limit:
            deque_people.appendleft(left) # right만 태움 : queue에서 뺌
        result += 1
    return result