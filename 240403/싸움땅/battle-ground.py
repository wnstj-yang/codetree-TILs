# 2024-04-02


def is_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


def move_loser(l):
    x, y, d, s, g = players[l]
    if g != 0:
        board[x][y].append(g)
    g = 0
    nd = d
    is_player = False
    for k in range(4):
        nx = x + dx[nd]
        ny = y + dy[nd]
        if not is_range(nx, ny):
            nd = (nd + 1) % 4
            continue
        for z in range(M):
            if l != z:
                tx, ty = players[z][0], players[z][1]
                if nx == tx and ny == ty:
                    is_player = True
                    break
        if not is_player:
            if board[nx][ny]:
                max_value = max(board[nx][ny])
                if g < max_value:
                    players[l] = [nx, ny, nd, s, max_value]
                    board[nx][ny].remove(max_value)
                    if g != 0:
                        board[nx][ny].append(g)
            else:
                players[l] = [nx, ny, nd, s, g]
            break
        else:
            nd = (nd + 1) % 4


def fight(n, t):
    x, y, d, s, g = players[n]
    tx, ty, td, ts, tg = players[t]
    source = s + g
    target = ts + tg
    win, lost = n, t
    if source < target:
        win, lost = t, n
    elif source == target:
        if s < ts:
            win, lost = t, n
    move_loser(lost)
    wx, wy, wd, ws, wg = players[win]
    if board[wx][wy]:
        max_value = max(board[wx][wy])
        if wg < max_value:
            players[win] = [wx, wy, wd, ws, max_value]
            board[wx][wy].remove(max_value)
            if wg != 0:
                board[wx][wy].append(wg)
    else:
        players[win] = [wx, wy, wd, ws, wg]
    result[win] += abs(source - target)


def move_player(index):
    x, y, d, s, g = players[index]
    nx = x + dx[d]
    ny = y + dy[d]

    is_player = False
    if not is_range(nx, ny):
        d = (d + 2) % 4
        nx = x + dx[d]
        ny = y + dy[d]
    for i in range(M):
        if i != index:
            tx, ty = players[i][0], players[i][1]
            if tx == nx and ty == ny:
                is_player = True
                players[index][0], players[index][1], players[index][2] = nx, ny, d
                fight(index, i)
                break

    if not is_player:
        players[index] = [nx, ny, d, s, g]
        if board[nx][ny]:
            max_value = max(board[nx][ny])
            if g < max_value:
                players[index] = [nx, ny, d, s, max_value]
                board[nx][ny].remove(max_value)
                if g != 0:
                    board[nx][ny].append(g)


N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
gun_info = [list(map(int, input().split())) for _ in range(N)]
players = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = [0] * M
for i in range(N):
    for j in range(N):
        if gun_info[i][j]:
            board[i][j].append(gun_info[i][j])

for i in range(M):
    x, y, d, s = map(int, input().split())
    players.append([x - 1, y - 1, d, s, 0]) # [x, y 좌표, 방향, 초기 능력치, 가지고 있는 총]

for _ in range(K):
    for i in range(M):
        move_player(i)

print(*result)