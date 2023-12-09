# 2023-12-09

from collections import deque


# 1. 공격자 선정
def search_weakest():
    global ax, ay

    # 1. 가장 약한 포탑 값
    min_value = 987654321
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                min_value = min(min_value, board[i][j])
    weak_list = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == min_value:
                weak_list.append((attacked[i][j], i + j, i, j))
    weak_list.sort(key=lambda x:(-x[0], -x[1], -x[3]))
    ax, ay = weak_list[0][2], weak_list[0][3]
    board[ax][ay] += (N + M)


# 2. 공격 받는자 선정
def search_strongest():
    global sx, sy

    max_value = 0
    for i in range(N):
        for j in range(M):
            if i == ax and j == ay:
                continue
            if board[i][j] > 0:
                max_value = max(max_value, board[i][j])

    strong_list = []
    for i in range(N):
        for j in range(M):
            if i == ax and j == ay:
                continue
            if board[i][j] == max_value:
                strong_list.append((attacked[i][j], i + j, i, j))
    strong_list.sort(key=lambda x:(x[0], x[1], x[2]))
    sx, sy = strong_list[0][2], strong_list[0][3]


# 2. 레이저, 포탑 공격
def attack():
    q = deque()
    q.append((ax, ay, []))
    visited = [[False] * M for _ in range(N)]
    visited[ax][ay] = True
    attack_value = board[ax][ay] // 2
    is_laser = False
    while q:
        x, y, path = q.popleft()
        if x == sx and y == sy:
            is_laser = True
            for px, py in path:
                if px == sx and py == sy:
                    board[px][py] -= board[ax][ay]
                else:
                    board[px][py] -= attack_value
                attack_status[px][py] = True
            break
        for d in range(4):
            nx = (x + dx[d]) % N
            ny = (y + dy[d]) % M
            if not visited[nx][ny] and board[nx][ny] > 0:
                q.append((nx, ny, path + [(nx, ny)]))
                visited[nx][ny] = True

    if not is_laser:
        board[sx][sy] -= board[ax][ay]

        for d in range(8):
            nx = (sx + dx[d]) % N
            ny = (sy + dy[d]) % M
            if nx == ax and ny == ay:
                continue
            if board[nx][ny] > 0:
                attack_status[nx][ny] = True
                board[nx][ny] -= attack_value
                if board[nx][ny] < 0:
                    board[nx][ny] = 0

    for i in range(N):
        for j in range(M):
            if board[i][j] < 0:
                board[i][j] = 0
    repair()


def repair():
    for i in range(N):
        for j in range(M):
            if not attack_status[i][j] and board[i][j] > 0:
                board[i][j] += 1


N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
attacked = [[0] * M for _ in range(N)]
# 우하좌상 + 대각선
dx = [0, 1, 0, -1, -1, -1, 1, 1]
dy = [1, 0, -1, 0, -1, 1, 1, -1]

for t in range(1, K + 1):
    attack_status = [[False] * M for _ in range(N)]
    ax, ay = -1, -1
    sx, sy = -1, -1
    search_weakest()
    attacked[ax][ay] = t
    attack_status[ax][ay] = True
    attack_status[sx][sy] = True
    search_strongest()
    attack()
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                cnt += 1
    if cnt == 1:
        break

answer = 0
for i in range(N):
    for j in range(M):
        answer = max(answer, board[i][j])
print(answer)