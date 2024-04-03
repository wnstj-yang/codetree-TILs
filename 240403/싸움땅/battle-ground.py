# 2024-04-02


def is_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


def move_loser(l):
    x, y, d, s, g = players[l]
    # 진 플레이어기 때문에 본인이 가지고 있는 총을 내려 놓는다
    if g != 0:
        board[x][y].append(g)
    g = 0
    players[l][4] = 0
    nd = d
    for _ in range(4):
        is_player = False # 순회하면서 초기화해주지 않으면 플레이어가 있다고 보는 상태에서 다음 방향에 비어있다고 해도 방향 전환만 다시 하게 됨
        nx = x + dx[nd]
        ny = y + dy[nd]
        if not is_range(nx, ny):
            nd = (nd + 1) % 4
            continue
        for z in range(M):
            if z != l:
                tx, ty = players[z][0], players[z][1]
                if nx == tx and ny == ty:
                    is_player = True
                    break
        if is_player:
            nd = (nd + 1) % 4
        else:
            players[l] = [nx, ny, nd, s, 0]
            break
    if board[nx][ny]:
        max_value = max(board[nx][ny])

        if g < max_value:
            players[l][-1] = max_value
            board[nx][ny].remove(max_value)
            if g != 0:
                board[nx][ny].append(g)


# n은 지금 이동하는 플레이어, t는 같은 위치에 있는 플레이어 들의 인덱스
def fight(n, t):
    x, y, d, s, g = players[n]
    tx, ty, td, ts, tg = players[t]
    source = s + g
    target = ts + tg
    win, lost = n, t # 이긴 플레이어, 지는 플레이어 미리 설정
    # 초기 능력치와 총의 합이 둘 다 같은 경우
    if source == target:
        # target이 되는 플레이어의 초기 능력치가 큰 경우 인덱스 뒤바꿈
        if s < ts:
            win, lost = t, n
    # 같은 위치에 있는 값이 더 큰 경우 인덱스 뒤바꿈
    elif source < target:
        win, lost = t, n
    result[win] += abs(source - target)

    move_loser(lost) # 진플레이어 먼저 이동
    x, y, d, s, g = players[win]
    if board[x][y]:
        max_value = max(board[x][y])
        if g < max_value:
            players[win][-1] = max_value
            board[x][y].remove(max_value)
            if g != 0:
                board[x][y].append(g)


def move_player(index):
    x, y, d, s, g = players[index]
    nx = x + dx[d]
    ny = y + dy[d]
    # 범위를 벗어나지 않을 경우 방향 반대로 전환 후 이동
    if not is_range(nx, ny):
        d = (d + 2) % 4
        nx = x + dx[d]
        ny = y + dy[d]
    players[index][0], players[index][1], players[index][2] = nx, ny, d # 현재 플레이어 좌표 및 방향 갱신
    is_player = False
    for i in range(M):
        if i != index:
            tx, ty = players[i][0], players[i][1]
            if tx == nx and ty == ny:
                is_player = True
                fight(index, i) # index: 이동하는 플레이어 / i : 이동한 곳에 있는 플레이어
                break

    if not is_player:
        if board[nx][ny]:
            max_value = max(board[nx][ny])
            if g < max_value:
                players[index][4] = max_value
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