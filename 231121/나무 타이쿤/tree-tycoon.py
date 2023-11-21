# 2023-11-21
# 20:50 ~


def move_nutrients(d, p):
    next_nutrients = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if nutrients[i][j]:
                nx = (i + dx[d] * p) % N
                ny = (j + dy[d] * p) % N
                next_nutrients[nx][ny] = True
                board[nx][ny] += 1

    return next_nutrients


def grow():
    for i in range(N):
        for j in range(N):
            if nutrients[i][j]:
                cnt = 0
                for k in range(8):
                    if k % 2:
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue
                        if board[nx][ny] >= 1:
                            cnt += 1
                board[i][j] += cnt


def cut():
    for i in range(N):
        for j in range(N):
            if not nutrients[i][j] and board[i][j] >= 2:
                nutrients[i][j] = True
                board[i][j] -= 2
            elif nutrients[i][j]:
                nutrients[i][j] = False


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# 조건에 나와있는 방향
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
nutrients = [[False] * N for _ in range(N)]
nutrients[N - 1][0] = True
nutrients[N - 1][1] = True
nutrients[N - 2][0] = True
nutrients[N - 2][1] = True
for _ in range(M):
    d, p = map(int, input().split())
    d -= 1
    nutrients = move_nutrients(d, p)
    grow()
    cut()
total = 0
for i in board:
    total += sum(i)
print(total)