# 2023-12-03
#


def search(target):
    for i in range(N):
        for j in range(N):
            if state[i][j]:
                for index, info in enumerate(state[i][j]):
                    num, d = info
                    if num == target:
                        return [i, j, d, index]


def change_direction(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    else:
        return 2


def move(x, y, d, idx, target):
    nx = x + dx[d]
    ny = y + dy[d]
    is_red = False
    # 격자를 벗어날 떄 방향 전환
    if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:
        d = change_direction(d)
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:
            nx, ny = x, y
        elif board[nx][ny] == 1:
            is_red = True
    elif board[nx][ny] == 1:
        is_red = True

    group = state[x][y][idx:]
    del state[x][y][idx:]

    group[0] = (target, d)

    if is_red:
        group.reverse()

    state[nx][ny].extend(group)

    if len(state[nx][ny]) >= 4:
        return True
    return False


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
state = [[[] for _ in range(N)] for _ in range(N)]
# 우좌상하
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(1, K + 1):
    x, y, d = map(int, input().split())
    state[x - 1][y - 1].append((i, d - 1))
turn = 1
found = False
while turn < 1000:
    for i in range(1, K + 1):
        x, y, d, idx = search(i)
        if move(x, y, d, idx, i):
            found = True
            break

    if found:
        break

    turn += 1
if found:
    print(turn)
else:
    print(-1)