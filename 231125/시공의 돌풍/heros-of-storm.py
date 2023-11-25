# 2023-11-25
# 18:00 ~


def spread(x, y):
    num = board[x][y] // 5
    if num < 1:
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or board[nx][ny] == -1:
            continue
        add_board[nx][ny] += num
        board[x][y] -= num


def add():
    for i in range(N):
        for j in range(M):
            board[i][j] += add_board[i][j]


def clean(x, y, direction):
    nx = x + dx[0]
    ny = y + dy[0]
    number = board[nx][ny]
    board[nx][ny] = 0
    # d가 True면 반시계, False면 시계방향 즉, 돌풍의 위와 아래 시작점
    if direction:
        for i in range(4):
            while True:
                next_x = nx + dx[i]
                next_y = ny + dy[i]
                if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
                    break
                if next_x == x and next_y == y:
                    return
                nx, ny = next_x, next_y
                temp = board[nx][ny]
                board[nx][ny] = number
                number = temp

    else:
        for i in range(4):
            d = i
            if i == 1 or i == 3:
                d = (d + 2) % 4
            while True:
                next_x = nx + dx[d]
                next_y = ny + dy[d]
                if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
                    break
                if next_x == x and next_y == y:
                    return
                nx, ny = next_x, next_y
                temp = board[nx][ny]
                board[nx][ny] = number
                number = temp


N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
wind = []
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
for i in range(N):
    for j in range(M):
        if board[i][j] == -1:
            wind.append((i, j))

while T:
    add_board = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                spread(i, j)
    add()

    clean(wind[0][0], wind[0][1], True)
    clean(wind[1][0], wind[1][1], False)
    T -= 1

total = 0
for i in range(N):
    for j in range(M):
        if board[i][j]:
            total += board[i][j]
print(total + 2)