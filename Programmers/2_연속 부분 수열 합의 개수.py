elements = [7,9,1,1,4]

from collections import deque
from itertools import islice

def solution(elements):
    answer = []
    dq = deque(elements)
    for l in range(1, len(elements) + 1):
        rotate = 0
        while rotate < len(elements):
            curr = sum(list(islice(dq, 0, l)))
            if curr not in answer:
                answer.append(curr)
            dq.rotate(1)
            rotate += 1

    return len(answer)

solution(elements)
'''
    정확성 : 2 / 20 
    (시간초과)
'''
def solution(elements):
    answer = []
    L = len(elements)
    for l in range(1, L + 1):
        left = 0
        right = left + l
        while left < L:
            # print(left, right)
            if right < L:
                curr_sum = sum(elements[left:right])
            else:
                curr_sum = sum(elements[left:] + elements[:right - L])

            if curr_sum not in answer:
                answer.append(curr_sum)

            left += 1
            right += 1

    return len(answer)
'''
    정확성 : 2 / 20 
    (시간초과)
'''

def solution(elements):
    answer = set()
    L = len(elements)
    elements *= 2
    for l in range(1, L + 1):
        for i in range(L):
            answer.add(sum(elements[i:i + l]))

    return len(answer)




def solution(elements):
    ll = len(elements)
    res = set()

    for i in range(ll):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i+1, i+ll):
            ssum += elements[j%ll]
            res.add(ssum)
    return len(res)