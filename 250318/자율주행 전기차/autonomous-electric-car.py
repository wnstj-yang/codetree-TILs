from collections import deque

def is_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True

def search(sx, sy):
    global C

    if board[sx][sy] > 1:
        return [sx, sy, board[sx][sy]]

    cx, cy, battery = sx, sy, C
    visited = [[False] * N for _ in range(N)]
    visited[cx][cy] = True
    q = deque()
    q.append((cx, cy, battery))
    candidates = []
    while q:
        x, y, b = q.popleft()
        if b <= 0:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_range(nx, ny) and not visited[nx][ny] and board[nx][ny] != 1:
                visited[nx][ny] = True
                if board[nx][ny] > 1:
                    candidates.append((b - 1, nx, ny, board[nx][ny]))
                q.append((nx, ny, b - 1))
    if candidates:
        candidates.sort(key=lambda x:(-x[0], x[1], x[2]))
        b, x, y, num = candidates[0]
        C = b
        return [x, y, num]
    # 사람을 못태웠다면 기름이 부족해서이므로 끝
    else:
        return [-1, -1, -1]


def find_flag(sx, sy, target):
    battery = C
    q = deque()
    q.append((sx, sy, battery))
    visited = [[False] * N for _ in range(N)]
    visited[sx][sy] = True
    ex, ey = positions[target]
    while q:
        x, y, b = q.popleft()
        if b <= 0:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_range(nx, ny) and not visited[nx][ny] and board[nx][ny] != 1:
                if nx == ex and ny == ey:
                    del positions[target]
                    return [nx, ny, (b - 1) + (battery - (b - 1)) * 2]
                visited[nx][ny] = True
                q.append((nx, ny, b - 1))
    return [-1, -1, -1]

N, M, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
sx, sy = map(int, input().split())
sx -= 1
sy -= 1
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
positions = {}
for i in range(M):
    xs, ys, xe, ye = map(int, input().split())
    positions[i + 2] = [xe - 1, ye - 1]
    board[xs - 1][ys - 1] = i + 2

result = -1
# print('처음')
# print(positions)
# for z in board:
#     print(z)
while positions:

    sx, sy, target = search(sx, sy)
    if sx == -1:
        break
    board[sx][sy] = 0
    # print('search', sx, sy, result)
    sx, sy, C = find_flag(sx, sy, target)
    result = C
    if sx == -1:
        break
    # print('find', sx, sy, result)
    # print(positions)
    # for z in board:
    #     print(z)
    # print('---------', sx, sy, result)
print(result)


