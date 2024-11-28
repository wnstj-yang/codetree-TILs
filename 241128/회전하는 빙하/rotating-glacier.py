from collections import deque

def divide_rotate(x, y, d, step, arr, new):
    for a in range(x, x + step):
        for b in range(y, y + step):
            nx = a + dx[d] * step
            ny = b + dy[d] * step
            new[nx][ny] = arr[a][b]


def rotate(l):
    level = 2 ** l
    step = 2 ** (l - 1)
    new_board = [[0] * length for _ in range(length)]
    for i in range(0, length, level):
        for j in range(0, length, level):
            divide_rotate(i, j, 0, step, board, new_board)
            divide_rotate(i, j + step, 1, step, board, new_board)
            divide_rotate(i + step, j + step, 2, step, board, new_board)
            divide_rotate(i + step, j, 3, step, board, new_board)
    return new_board

def melt():
    melt_list = []
    for x in range(2 ** n):
        for y in range(2 ** n):
            cnt = 0
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or nx >= length or ny < 0 or ny >= length:
                    continue
                if board[nx][ny]:
                    cnt += 1
            if cnt < 3:
                melt_list.append((x, y))
    for x, y in melt_list:
        if board[x][y]:
            board[x][y] -= 1

n, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2 ** n)]
order = list(map(int, input().split()))
length = 2 ** n
# 우하좌상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for o in order:
    if o:
        board = rotate(o)
    melt()
total = 0
for row in board:
    total += sum(row)
size = 0
visited = [[False] * (2 ** n) for _ in range(2 ** n)]
for i in range(length):
    for j in range(length):
        if board[i][j] and not visited[i][j]:
            q = deque()
            q.append((i, j))
            visited[i][j] = True
            cnt = 1
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or nx >= length or ny < 0 or ny >= length:
                        continue
                    if not visited[nx][ny] and board[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        cnt += 1
            size = max(size, cnt)
print(total)
print(size)
