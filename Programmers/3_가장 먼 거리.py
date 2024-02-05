from collections import defaultdict, deque

inf = float('inf')

n = 6
edge = 	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for n1, n2 in edge:
        graph[n1].append(n2)
        graph[n2].append(n1)

    dists = [-1] * (n+1)
    q = deque([1])
    dists[1] = 0

    while q:
        c_n = q.popleft()

        for node in graph[c_n]:
            if dists[node] == -1:
                dists[node] = dists[c_n] + 1
                q.append(node)

    answer = dists.count(max(dists))
    return answer

print(solution(n, edge))