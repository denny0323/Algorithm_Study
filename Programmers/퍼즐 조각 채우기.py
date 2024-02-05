import copy

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

empty = []
blocks = []


def find_space(x, y, N, visited, MAP, check):
    space = [(x, y)]
    q = [(x, y)]
    visited[x][y] = True

    while q:
        cx, cy = q.pop(0)

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if not visited[nx][ny] and MAP[nx][ny] == check:
                visited[nx][ny] = True
                space.append((nx, ny))
                q.append((nx, ny))

    return sorted(space)


def rotate(block, N):
    return sorted([(by, N - 1 - bx) for bx, by in block])


def standard(block):
    min_x = min([b for b, _ in block])
    min_y = min([b for _, b in block])
    return sorted([(bx - min_x, by - min_y) for bx, by in block])


def solution(game_board, table):
    global answer
    answer = 0

    empty = []
    blocks = []

    N = len(game_board)

    visited_board = [[False] * N for _ in range(N)]
    visited_table = [[False] * N for _ in range(N)]

    ## 1. 같은 위상을 확인하며 board에서는 빈칸 좌표를, table에서는 블록 좌표를 저장
    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 0 and not visited_board[i][j]:
                empty.append(find_space(i, j, N, visited_board, game_board, 0))

            if table[i][j] == 1 and not visited_table[i][j]:
                blocks.append(find_space(i, j, N, visited_table, table, 1))

    ## 2. 빈칸, 블록을 표준화
    empty_std = [standard(e) for e in empty]
    blocks_std = [standard(b) for b in blocks]

    # print(empty_std)
    # print(blocks_std)
    ## 3. 블록과 빈칸을 matching해보기

    for b_std in blocks_std:
        # print('찾는', b_std)
        if b_std in empty_std:  # 그대로 일치 확인
            # print('찾음')
            answer += len(b_std)
            empty_std.remove(b_std)  ## 들어간 블록은 빼주기

        else:  # 회전시켜서 확인
            for e_std in empty_std:
                # print('회전해서 확인', e_std)
                e_std_tmp = copy.copy(e_std)
                for r in range(4):
                    if b_std == e_std_tmp:
                        # print('회전해서 찾음', e_std_tmp)
                        answer += len(b_std)
                        empty_std.remove(e_std)
                        break
                    e_std_tmp = standard(rotate(e_std_tmp, N))
                    # print('회전한 결과', e_std_tmp)
    return answer


game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]

solution(game_board, table)