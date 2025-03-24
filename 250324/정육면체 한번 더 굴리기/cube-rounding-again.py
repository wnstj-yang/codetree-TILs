from collections import deque

def is_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


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


def calculate(x, y):
    q = deque()
    q.append((x, y))
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    target = board[x][y]
    cnt = 1
    while q:
        tx, ty = q.popleft()
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if is_range(nx, ny) and not visited[nx][ny] and board[nx][ny] == target:
                visited[nx][ny] = True
                cnt += 1
                q.append((nx, ny))
    return cnt * target


# 상하좌우
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
total = 0
dice = [1, 4, 5, 3, 6, 2]
cx, cy = 0, 0
d = 0
for _ in range(M):
    nx = cx + dx[d]
    ny = cy + dy[d]
    if not is_range(nx, ny):
        d = (d + 2) % 4
        nx = cx + dx[d]
        ny = cy + dy[d]
    rotate(d)
    cx, cy = nx, ny
    total += calculate(cx, cy)
    if dice[4] > board[cx][cy]:
        d = (d + 1) % 4
    elif dice[4] < board[cx][cy]:
        d = (d - 1) % 4
print(total)
