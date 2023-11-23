# 2023-11-23
# 21:25 ~ 23:33

from collections import deque


def dfs(idx, cnt):
    global time

    if cnt == M:
        delete_virus()
        return

    for i in range(idx, len(hospitals)):
        if not visited[i]:
            visited[i] = True
            candi[cnt] = i
            dfs(i, cnt + 1)
            visited[i] = False


def delete_virus():
    global time

    q = deque()
    time_visited = [[False] * N for _ in range(N)]
    steps = [[0] * N for _ in range(N)]
    max_time = 0
    for i in candi:
        x, y = hospitals[i]
        q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if board[nx][ny] != 1 and not time_visited[nx][ny]:
                steps[nx][ny] = steps[x][y] + 1
                time_visited[nx][ny] = True
                q.append((nx, ny))

    
    is_left = False
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                if not time_visited[i][j]:
                    is_left = True
                    break
                else:
                    max_time = max(max_time, steps[i][j])

        if is_left:
            break
    if not is_left:

        time = min(max_time, time)


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
hospitals = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            hospitals.append((i, j))
time = 987654321
candi = [0] * M
visited = [False] * len(hospitals)
dfs(0, 0)
if time == 987654321:
    time = -1
print(time)