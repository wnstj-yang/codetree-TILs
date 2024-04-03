# 2024-04-03

from collections import deque


def is_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


def search(x, y):
    visited[x][y] = True
    num = board[x][y]
    q = deque()
    q.append((x, y))
    group = [(x, y)]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if is_range(nx, ny) and not visited[nx][ny] and board[nx][ny] == num:
                visited[nx][ny] = True
                group.append((nx, ny))
                q.append((nx, ny))

    return group


def check_border(first, second):
    cnt = 0
    second_num = board[second[0][0]][second[0][1]]
    for x, y in first:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if is_range(nx, ny) and board[nx][ny] == second_num and (nx, ny) in second:
                cnt += 1
    return cnt


def dfs(idx, k):
    global result

    if k == 2:
        first, second = groups[pair[0]], groups[pair[1]]
        first_num = board[first[0][0]][first[0][1]]
        second_num = board[second[0][0]][second[0][1]]
        border_cnt = check_border(first, second)
        result += ((len(first) + len(second)) * first_num * second_num * border_cnt)
        return

    for i in range(idx, len(groups)):
        pair[k] = i
        dfs(i + 1, k + 1)


def rotate():
    next_board = [[0] * N for _ in range(N)]
    mid = N // 2
    # 0. 중앙 십자가 이동
    for i in range(N):
        next_board[mid][i] = board[i][mid]
        next_board[N - 1 - i][mid] = board[mid][i]
    # 1. 왼쪽 상단
    for i in range(mid):
        for j in range(mid):
            next_board[j][mid - i - 1] = board[i][j]
    # 2. 오른쪽 상단
    for i in range(mid):
        for j in range(mid + 1, N):
            next_board[j - mid - 1][N - 1 - i] = board[i][j]
    # 3. 왼쪽 하단
    for i in range(mid + 1, N):
        for j in range(mid):
            next_board[mid + 1 + j][N - i - 1] = board[i][j]

    # 4. 오른쪽 하단
    for i in range(mid + 1, N):
        for j in range(mid + 1, N):
            next_board[j][N - (i - mid)] = board[i][j]
    return next_board


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
groups = []
pair = [0] * 2
for _ in range(4):
    groups = []
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                groups.append(search(i, j))
    dfs(0, 0)
    board = rotate()
print(result)