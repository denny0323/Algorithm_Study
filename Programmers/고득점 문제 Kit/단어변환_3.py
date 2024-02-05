begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

# word_to_chr_list = [list(word) for word in words]
# word_to_chr_list.append(list(begin))
#
# from collections import defaultdict
#
# word_level = defaultdict(list)
# for i in range(len(word_to_chr_list)-1):
#     for j in range(i+1, len(word_to_chr_list)):
#         level = sum([word_to_chr_list[j][k] != word_to_chr_list[i][k] for k in range(len(begin))])
#         if level == 1:
#             word_level[''.join(word_to_chr_list[i])].append(''.join(word_to_chr_list[j]))
#
# word_visited = {word:False for word in word_to_chr_list}
#
# def DFS(begin, target, step):
#     if begin == target:
#         return step
#
#     DFS(begin, word_visited)
#
#
#
# def solution(begin, target, words):
#     global step
#     step = 0
#     if target not in words:
#         return step


from collections import deque
def solution(begin, target, words):
    queue = deque([(begin, words, 0)])

    while queue:
        for item in range(len(queue)):
            word, words, count = queue.popleft()

            if word == target:
                return count

            for i, item in enumerate(words):
                if len(set(word) - set(item)) == 1: # 인접단어 <-- 창의적인데, 이 부분 때문에 통과가 안됨
                    queue.append((item, words[:i] + words[i + 1 :], count + 1))

    return 0



## 다른 인접단어 찾기
def solution(begin, target, words):
    if target not in words:
        return 0

    answer = 0
    visited = [0 for _ in range(len(words))]
    stacks = [begin]

    while stacks:
        stack = stacks.pop()

        if stack == target:
            return answer

        for i in range(len(words)):
            if len([j for j in range(len(words[i])) if words[i][j] != stack[j]]) == 1:
                if not visited[i]:
                    visited[i] = 1
                    stacks.append(words[i])
        answer += 1
    return answer



from collections import deque
def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word

def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)