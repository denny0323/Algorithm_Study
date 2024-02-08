from collections import deque

s = "[](){}"

from collections import deque, Counter


def IsCorrect(dq):
    # 개수
    counter = Counter(dq)
    if counter['('] != counter[')']: return False
    if counter['['] != counter[']']: return False
    if counter['{'] != counter['}']: return False

    # 올바른 문자열인지 판별
    s_open = False;
    s_close = False
    m_open = False;
    m_close = False
    l_open = False;
    l_close = False

    for ss in dq:
        if ss == '(':
            s_open = True
        elif ss == ')':
            if s_open:
                s_close = True
            else:
                return False

        elif ss == '[':
            m_open = True
        elif ss == ']':
            if m_open:
                m_close = True
            else:
                return False

        elif ss == '{':
            l_open = True
        elif ss == '}':
            if l_open:
                l_close = True
            else:
                return False
    return all([s_open, s_close, m_open, m_close, l_open, l_close])

# def solution(s):
#     L = len(s)
#     dq = deque(s)
#     answer = []
#     for _ in range(L):
#         dq.rotate(-1)
#         print(dq)
#         answer.append(IsCorrect(dq))
#         print(IsCorrect(dq))
#     return sum(answer)

# solution(s)
'''
    4 / 14
    정확성 : 28.6 / 100.0
'''

s = "((()))"
def solution(s):
    cnt = 0
    for i in range(len(s)):
        tmp = s[i:] + s[:i]  # 회전
        while True:
            tmp_l = len(tmp)
            tmp = tmp.replace("()", "")
            tmp = tmp.replace("[]", "")
            tmp = tmp.replace("{}", "")

            if len(tmp) == 0:
                cnt += 1
                break

            if tmp_l == len(tmp):  # 소거 안됨
                break

    return cnt

print(solution(s))