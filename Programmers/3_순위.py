n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

from collections import defaultdict

#def solution(n, results):
win, lose = defaultdict(set), defaultdict(set)

for win_, los_ in results:
    win[win_].add(los_)  # i가 이긴 선수들
    lose[los_].add(win_)  # i를 이긴 선수들

for i in range(1, n + 1):
    for winner in lose[i]:
        win[winner].update(win[i])  # i를 이긴 선수들은 i가 이긴 선수들을 가져감
    for loser in win[i]:
        lose[loser].update(lose[i])  # i가 이긴 선수들은 i를 이긴 선수들을 가져감

answer = 0
for i in range(1, n + 1):
    if len(win[i]) + len(lose[i]) == (n - 1):
        answer += 1

#return answer

print(win)
print(lose)