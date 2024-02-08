k = 6; tangerine = [1, 3, 2, 5, 4, 5, 2, 3];


from collections import Counter
def solution(k, tangerine):
    select = []
    sorted_tangerine = sorted([(size, cnt) for size, cnt in Counter(tangerine).items()], key=lambda x:-x[1])
    for size, cnt in sorted_tangerine:
        print(select)
        if k <= 0:
            return len(select)
        select.append(size)
        k -= cnt
    return len(select)

#solution(k, tangerine)