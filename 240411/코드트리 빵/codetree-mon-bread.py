# 2024-04-11

from collections import deque


def is_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


# 1. 격자판 안에 있는 사람들 이동 + 편의점 도착 시 움직이지 못하는 칸 처리
def move():
    global total

    next_people = []
    arrived = []
    for num, x, y in people:
        md = 0
        min_cnt = 987654321
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_range(nx, ny) and allowed[nx][ny]:
                q = deque()
                q.append((nx, ny, 1))
                visited = [[False] * N for _ in range(N)]
                visited[nx][ny] = True
                while q:
                    r, c, cnt = q.popleft()
                    if board[r][c] == num:
                        if min_cnt > cnt:
                            min_cnt = cnt
                            md = i
                        break
                    for d in range(4):
                        nr = r + dx[d]
                        nc = c + dy[d]
                        if is_range(nr, nc) and not visited[nr][nc] and allowed[nr][nc]:
                            q.append((nr, nc, cnt + 1))
                            visited[nr][nc] = True
        nx = x + dx[md]
        ny = y + dy[md]
        if board[nx][ny] == num:
            arrived.append((nx, ny))
        else:
            next_people.append((num, nx, ny))

    if arrived:
        for x, y in arrived:
            allowed[x][y] = False
            total += 1
    return next_people



def move_first(num, x, y):
    q = deque()
    q.append((x, y, 0))
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    arrived = []
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_range(nx, ny) and not visited[nx][ny] and allowed[nx][ny]:
                if board[nx][ny] == 1:
                    allowed[nx][ny] = False
                    people.append((num, nx, ny))
                    return
                visited[nx][ny] = True
                q.append((nx, ny, cnt + 1))



N, M = map(int, input().split())
allowed = [[True] * N for _ in range(N)] # 갈 수 있는지에 대한 격자판
board = [list(map(int, input().split())) for _ in range(N)] # 빈 칸 및 베이스캠프 존재 격자판
people = []
people_q = deque()
total = 0
time = 1
# 상좌우하
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
for i in range(2, M + 2):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = i # 편의점
    people_q.append((i, x - 1, y - 1))

while True:
    # 1. 격자판에 사람이 존재하는 경우 1칸 이동 / 갱신
    people = move()
    if total == M:
        break
    if time <= M:
        num, x, y = people_q.popleft()
        move_first(num, x, y)

    time += 1

print(time)