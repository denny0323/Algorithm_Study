def FindNoIncen(scores):
    Incen = []
    for i in range(len(scores)):
        is_break = False
        for j in range(len(scores)):
            if scores[i][1][0] < scores[j][1][0] and scores[i][1][1] < scores[j][1][1]:
                is_break = True
                break
        if not is_break:
            Incen.append(scores[i])
    return sorted(Incen, key=lambda x:x[0])


from itertools import groupby

def solution(scores):
    scores = [(i, score) for i, score in enumerate(scores)]
    scores = FindNoIncen(scores)

    sorted_scres = sorted(scores, key=lambda x: -sum(x[1]))
    ranks = []
    rank = 1
    for k, v in groupby(sorted_scres, lambda x: -sum(x[1])):
        grp = [(rank, tup) for tup in v]
        ranks += grp
        rank += len(grp)

    ranks.sort(key=lambda x: x[1][0])
    if ranks[0][1][0] == 0:
        return ranks[0][0]
    else:
        return -1

'''
    result : 22/25 
    (시간초과: 테스트 21, 24, 25)
'''

