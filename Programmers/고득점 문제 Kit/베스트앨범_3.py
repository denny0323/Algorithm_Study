from itertools import chain
from collections import defaultdict

def solution(genres, plays):
    Counter = {}
    Playdict = defaultdict(list)
    for i, genre, play in zip(range(len(genres)), genres, plays):
        Playdict[genre].append((i, play))
        if not Counter.get(genre, 0):
            Counter[genre] = play
        else:
            Counter[genre] += play

    print(Playdict)
    for genre in Playdict.keys():
        if len(Playdict[genre]) >= 2:
            Playdict[genre] = sorted(Playdict[genre], key=lambda x: -x[1])[:2]

    MetaInfo = [[(id, genre, play) for id, play in id_play] for genre, id_play in Playdict.items()]
    MetaInfo = list(chain(*MetaInfo))
    MetaInfo.sort(key=lambda x: (-Counter[x[1]], -x[2], x[0]))
    print(MetaInfo)
    return [id for id, _, _ in MetaInfo]



genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


print(solution(genres, plays))
