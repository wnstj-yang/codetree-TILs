# 2024-03-20

from collections import deque


def is_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


# 묶음을 찾는다
def find_set(x, y):
    cnt, red = 1, 0
    color = board[x][y]
    q = deque()
    q.append((x, y))
    bx, sy = x, y
    red_list = []
    all_list = [(x, y)]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if is_range(nx, ny) and not visited[nx][ny] and (board[nx][ny] == 0 or board[nx][ny] == color):
                cnt += 1
                visited[nx][ny] = True
                all_list.append((nx, ny))
                q.append((nx, ny))
                if board[nx][ny] == 0:
                    red += 1
                    red_list.append((nx, ny))
                elif board[nx][ny] == color:
                    bx = max(nx, bx)
                    sy = min(ny, sy)

    for x, y in red_list:
        visited[x][y] = False
    if cnt >= 2:
        return [cnt, red, bx, sy, all_list]
    return []


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


# 반시계로 90도 회전
def rotate():
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[N - 1 - j][i] = board[i][j]
    return new_board


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0

while True:
    visited = [[False] * N for _ in range(N)]
    bombs = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and board[i][j] > 0:
                visited[i][j] = True
                result = find_set(i, j)
                if result:
                    bombs.append(result)
    if bombs:
        bombs.sort(key=lambda x:(-x[0], x[1], -x[2], x[3]))
        answer += (bombs[0][0] * bombs[0][0])
        for x, y in bombs[0][4]:
            board[x][y] = -2 # 빈칸

        gravity()
        board = rotate()
        gravity()

    else:
        break
print(answer)