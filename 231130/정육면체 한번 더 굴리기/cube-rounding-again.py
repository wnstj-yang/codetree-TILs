# 2023-11-29
# 20:58 ~ 22:25 / 23:35 ~ 24:01

from collections import deque


def rotate(d):
    # 우
    if d == 0:
        dice[0], dice[1], dice[4], dice[3] = dice[1], dice[4], dice[3], dice[0]
    # 하
    elif d == 1:
        dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0]
    # 좌
    elif d == 2:
        dice[0], dice[1], dice[4], dice[3] = dice[3], dice[0], dice[1], dice[4]
    # 상
    else:
        dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]


def get_score(x, y):
    number = board[x][y]
    q = deque()
    q.append((x, y))
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if not visited[nx][ny] and board[nx][ny] == number:
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1

    return cnt * number


# 우하좌상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
total = 0
dice = [1, 4, 5, 3, 6, 2]
# dice[3]이 정육면체의 밑면이 격자판과 맞닿은 부분
direc = 0
cx, cy = 0, 0
for _ in range(M):
    nx = cx + dx[direc]
    ny = cy + dy[direc]
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        direc = (direc + 2) % 4
        nx = cx + dx[direc]
        ny = cy + dy[direc]
    rotate(direc)
    cx, cy = nx, ny
    total += get_score(cx, cy)
    if dice[4] > board[cx][cy]:
        direc = (direc + 1) % 4
    elif dice[4] < board[cx][cy]:
        direc = (direc - 1) % 4

print(total)