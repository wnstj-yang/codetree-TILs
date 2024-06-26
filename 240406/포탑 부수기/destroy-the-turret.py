# 2024-04-06

from collections import deque


# 1. 공격자 선정
def select_attacker():
    weakest = 987654321
    for x in range(N):
        for y in range(M):
            if 0 < board[x][y] < weakest:
                weakest = board[x][y]
    weak_list = []
    for x in range(N):
        for y in range(M):
            if board[x][y] == weakest:
                weak_list.append((visited[x][y], x + y, x, y))

    weak_list.sort(key=lambda x: (-x[0], -x[1], -x[3]))
    x, y = weak_list[0][2], weak_list[0][3]
    board[x][y] += (N + M)
    return x, y


# 2. 공격자의 공격
def select_target():
    strongest = 0
    for x in range(N):
        for y in range(M):
            if x == wx and y == wy:
                continue
            if board[x][y] > 0 and strongest < board[x][y]:
                strongest = board[x][y]
    strong_list = []
    for x in range(N):
        for y in range(M):
            if x == wx and y == wy:
                continue
            if board[x][y] == strongest:
                strong_list.append((visited[x][y], x + y, x, y))

    strong_list.sort(key=lambda x: (x[0], x[1], x[3]))
    x, y = strong_list[0][2], strong_list[0][3]

    return x, y

# 2-1. 레이저 공격
def attack():
    q = deque()
    q.append((wx, wy, []))
    attack_visited = [[False] * M for _ in range(N)]
    attack_visited[wx][wy] = True
    half = board[wx][wy] // 2
    full = board[wx][wy]
    laser_result = []
    while q:
        x, y, coors = q.popleft()
        if x == ax and y == ay:
            laser_result = coors
            break

        for i in range(4):
            nx = (x + dx[i]) % N
            ny = (y + dy[i]) % M
            if board[nx][ny] > 0 and not attack_visited[nx][ny]:
                attack_visited[nx][ny] = True
                q.append((nx, ny, coors + [(nx, ny)]))

    if laser_result:
        for x, y in coors:
            if x == ax and y == ay:
                board[x][y] -= full
            else:
                board[x][y] -= half
            affected[x][y] = True
    else:
        board[ax][ay] -= full
        for i in range(8):
            nx = (ax + dx[i]) % N
            ny = (ay + dy[i]) % M
            if nx == wx and ny == wy:
                continue
            if board[nx][ny] > 0:
                board[nx][ny] -= half
                affected[nx][ny] = True


# 3. 포탄 부서짐 - 0이하된 포탑 0으로 초기화
def check_breaked():
    for x in range(N):
        for y in range(M):
            if board[x][y] < 0:
                board[x][y] = 0


# 4. 포탑 정비
def repair():
    for x in range(N):
        for y in range(M):
            if board[x][y] > 0 and not affected[x][y]:
                board[x][y] += 1


N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
# 우하좌상 + 왼쪽 위 대각선부터 시계방향으로 대각선 4방향
dx = [0, 1, 0, -1, -1, -1, 1, 1]
dy = [1, 0, -1, 0, -1, 1, 1, -1]
total = 0
for i in range(1, K + 1):
    wx, wy = select_attacker()  # 가장 약한 포탑
    ax, ay = select_target()  # 가장 강한 포탑
    affected = [[False] * M for _ in range(N)]
    affected[wx][wy] = True
    affected[ax][ay] = True
    visited[wx][wy] = i
    attack()
    check_breaked()
    repair()
    cnt = 0
    for x in range(N):
        for y in range(M):
            if board[x][y] > 0:
                cnt += 1
    if cnt == 1:
        break

for i in board:
    total = max(total, max(i))
print(total)