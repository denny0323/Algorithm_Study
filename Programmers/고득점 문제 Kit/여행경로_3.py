# ### test case 1번 런타임에러 --> 중복티켓을 고려
# def DFS(route, tickets):
#     print(route, tickets)
#     if tickets:
#         curr = route[-1]
#     else: # no tickets
#         answer.append(route)
#
#     togo = [ticket for ticket in tickets if ticket[0] == curr]
#     for nexts in togo:
#         remove_idx_first = tickets.index(nexts)
#         DFS(route+[nexts[1]], [v for i, v in enumerate(tickets) if i != remove_idx_first])
#
# def solution(tickets):
#     global answer
#     answer = []
#     DFS(["ICN"], tickets)
#     return answer

def solution(tickets):
    global answer
    answer = []

    DFS(["ICN"], tickets)
    answer.sort()
    return answer[0]


def DFS(route, tickets):
    if tickets:
        curr = route[-1]
    else:
        answer.append(route)

    ToGo = [ticket for ticket in tickets if ticket[0] == curr]
    for togo in ToGo:
        ToRemove = tickets.index(togo)
        DFS(route + [togo[1]], [v for i, v in enumerate(tickets) if i != ToRemove])


tickets = [["ICN","SFO"], ["ICN","ATL"], ["SFO","ATL"], ["ATL","ICN"], ["ATL","SFO"]]
print(solution(tickets))



