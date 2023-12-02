# 2023-12-02
# 14:20 ~

from collections import deque


def attack(d, p):
    global total

    for i in range(1, p + 1):
        nx = sx + dx[d] * i
        ny = sy + dy[d] * i
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            return
        total += board[nx][ny]
        board[nx][ny] = 0


def fill():
    length = 1
    cnt = 2
    direc = 0
    x, y = N // 2, N // 2
    empty = deque()
    while True:
        for _ in range(length):
            nx = x + dx[direc]
            ny = y + dy[direc]
            if board[nx][ny] == 0:
                empty.append((nx, ny))
            else:
                if empty:
                    ex, ey = empty.popleft()
                    board[ex][ey] = board[nx][ny]
                    board[nx][ny] = 0
                    empty.append((nx, ny))
            x, y = nx, ny
        if x == 0 and y == 0:
            return

        cnt -= 1
        direc = (direc + 1) % 4
        if cnt == 0:
            length += 1
            cnt = 2
            if length == N - 1:
                cnt = 3


def delete():
    global total

    length = 1
    cnt = 2
    direc = 0
    x, y = N // 2, N // 2
    same = deque((x, y))
    same_cnt = 1
    value = board[x][y]
    deleted = False
    while True:
        for _ in range(length):
            nx = x + dx[direc]
            ny = y + dy[direc]
            # 빈 공간 없이 채워져서 순회하므로 비어있다면 끝
            if board[nx][ny] == 0:
                return deleted

            if board[nx][ny] == value:
                same_cnt += 1
                same.append((nx, ny))
            else:
                if same_cnt >= 4:
                    deleted = True
                    for i, j in same:
                        total += board[i][j]
                        board[i][j] = 0
                same_cnt = 1
                same = [(nx, ny)]
                value = board[nx][ny]
            x, y = nx, ny

        if x == 0 and y == 0:
            if same_cnt >= 4:
                deleted = True
                for i, j in same:
                    board[i][j] = 0
            return deleted

        cnt -= 1
        direc = (direc + 1) % 4
        if cnt == 0:
            length += 1
            cnt = 2
            if length == N - 1:
                cnt = 3


def fill_pairs():
    next_board = [[0] * N for _ in range(N)]
    length = 1
    cnt = 2
    direc = 0
    x, y = N // 2, N // 2
    pairs = deque()
    same_cnt = 0
    value = 0
    is_end = False
    while True:
        for _ in range(length):
            nx = x + dx[direc]
            ny = y + dy[direc]
            if board[nx][ny] == 0:
                is_end = True
                break
            if board[nx][ny] == value:
                same_cnt += 1
            else:
                # 시작점부터 시작하기 때문에 해당 부분은 포함시키지 않는다.
                if same_cnt != 0:
                    pairs.extend([same_cnt, value])
                value = board[nx][ny]
                same_cnt = 1
            x, y = nx, ny
        if is_end or (x == 0 and y == 0):
            pairs.extend([same_cnt, value])
            break

        cnt -= 1
        direc = (direc + 1) % 4
        if cnt == 0:
            length += 1
            cnt = 2
            if length == N - 1:
                cnt = 3

    #  짝지어진 것을 다시 채워준다
    x, y = N // 2, N // 2
    length = 1
    cnt = 2
    direc = 0
    while True:
        for _ in range(length):
            nx = x + dx[direc]
            ny = y + dy[direc]
            if pairs:
                next_board[nx][ny] = pairs.popleft()
            else:
                return next_board
            x, y = nx, ny
        if x == 0 and y == 0:
            return next_board

        cnt -= 1
        direc = (direc + 1) % 4
        if cnt == 0:
            length += 1
            cnt = 2
            if length == N - 1:
                cnt = 3


# 좌하우상
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
sx, sy = N // 2, N // 2
total = 0
for _ in range(M):
    d, p = map(int, input().split())
    if d == 0 or d == 2:
        d = (d + 2) % 4
    attack(d, p)
    fill()
    while True:
        if not delete():
            break
        fill()
    board = fill_pairs()
print(total)