# 2024-04-12

from collections import deque


def is_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


def move():
    global total

    next_players = [[[] for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if players[x][y]:
                min_dist = abs(x - ex) + abs(y - ey)
                # is_moved = False
                for p in players[x][y]:
                    is_moved = False
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if is_range(nx, ny):
                            dist = abs(nx - ex) + abs(ny - ey)
                            if dist == 0:
                                total += 1
                                is_moved = True
                                players_state[p] = 0
                                break

                            if board[nx][ny] == 0 and min_dist > dist:
                                total += 1
                                is_moved = True
                                next_players[nx][ny].append(p)
                                break
                if not is_moved:
                    next_players[x][y].append(p)
    return next_players




def get_square():
    for l in range(2, N + 1):
        for i in range(N - l + 1):
            for j in range(N - l + 1):
                is_player = False
                is_exit = False
                for x in range(i, i + l):
                    for y in range(j, j + l):
                        if players[x][y]:
                            is_player = True
                        if x == ex and y == ey:
                            is_exit = True
                        if is_player and is_exit:
                            return [i, j, l]
    return []


def rotate(sx, sy, l):
    global ex, ey

    mid_board = [[0] * N for _ in range(N)]
    next_board = [[0] * N for _ in range(N)]
    mid_players = [[[] for _ in range(N)] for _ in range(N)]
    next_players = [[[] for _ in range(N)] for _ in range(N)]

    # 1. 먼저 0,0으로 옮기고 90도 회전 진행
    for i in range(sx, sx + l):
        for j in range(sy, sy + l):
            mid_board[i - sx][j - sy] = board[i][j]
            mid_players[i - sx][j - sy] = players[i][j]

    # 2. 0,0 기준으로 온 것에서 시계방향 90도 회전 진행
    for i in range(l):
        for j in range(l):
            next_board[j][l - 1 - i] = mid_board[i][j]
            next_players[j][l - 1 - i] = mid_players[i][j]
    # 3. 이제 기존 board로의 이동을 시켜준다
    for i in range(sx, sx + l):
        for j in range(sy, sy + l):
            board[i][j] = next_board[i - sx][j - sy]
            players[i][j] = next_players[i - sx][j - sy]
            if board[i][j] == 10:
                ex = i
                ey = j
                continue
            board[i][j] -= 1
            if board[i][j] < 0:
                board[i][j] = 0


N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
players = [[[] for _ in range(N)] for _ in range(N)]
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
total = 0
players_state = [1] * (M + 1)
for i in range(1, M + 1):
    x, y = map(int, input().split())
    players[x - 1][y - 1].append(i)
ex, ey = map(int, input().split())
ex -= 1
ey -= 1
board[ex][ey] = 10
for _ in range(K):
    if sum(players_state[1:]) == 0:
        break
    players = move()
    square = get_square()
    if square:
        x, y, l = square
        rotate(x, y, l)
print(total)
print(ex + 1, ey + 1)