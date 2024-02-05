n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

linked = {}
for i in range(n):
    linked[i+1] = [idx+1 for idx, node in enumerate(computers[i]) if node == 1]
print(linked)


answer = 1
visited = [False] * (n+1)
q = [1]  # start = 1
visited[0] = True
visited[1] = True

while q and not all(visited):
    cur = q.pop()

    for nxt in linked[cur]:
        if not visited[nxt]:
            q.append(nxt)
            visited[nxt] = True


    if len(q) == 0:
        q.append(visited.index(False))
        answer += 1 # 새로운 network의 시작

    print(q, answer)
print(answer)