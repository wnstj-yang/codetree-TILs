# 2023-11-12(일)


from collections import deque


def search(x, y):
    q = deque()
    q.append((x, y))
    color = board[x][y]
    visited[x][y] = True
    cnt = 1
    red = 0
    # 기준 점 좌표
    sx, sy = x, y
    red_list = []
    path = [(x, y)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if not visited[nx][ny] and (board[nx][ny] == color or board[nx][ny] == 0):
                cnt += 1
                q.append((nx, ny))
                path.append((nx, ny))
                visited[nx][ny] = True
                if board[nx][ny] == 0:
                    red += 1
                    red_list.append((nx, ny))
                else:
                    sx = max(sx, nx)
                    sy = min(sy, ny)
    for x, y in red_list:
        visited[x][y] = False
    if cnt >= 2:
        return [cnt, red, sx, sy, path]
    else:
        return []


# 중력 작용
def gravity():
    for j in range(N):
        cnt = 0
        for i in range(N - 1, -1, -1):
            if board[i][j] == -2:
                cnt += 1
            elif board[i][j] == -1:
                cnt = 0
            else:
                if cnt > 0:
                    board[i + cnt][j] = board[i][j]
                    board[i][j] = -2


# 반시계 90도
def rotate():
    next_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            next_board[N - j - 1][i] = board[i][j]
    return next_board


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
total = 0
while True:
    bombs = []
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and board[i][j] > 0:
                result = search(i, j)
                if len(result) > 0:
                    bombs.append(result)
    if len(bombs) == 0:
        break
    bombs.sort(key=lambda x:(-x[0], x[1], -x[2], x[3]))
    for x, y in bombs[0][4]:
        board[x][y] = -2
    gravity()
    board = rotate()
    gravity()
    total += (bombs[0][0] * bombs[0][0])
print(total)