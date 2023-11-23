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
    time_visited = [[False] * N for _ in range(N)] # 방문 표시
    steps = [[0] * N for _ in range(N)] # 단계
    max_time = 0 #
    # 인덱스로 받았던 조합을 좌표 값을 가지고 큐에 넣는다.
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

            # 벽이 아닌 곳과 방문하지 않았다면
            if board[nx][ny] != 1 and not time_visited[nx][ny]:
                steps[nx][ny] = steps[x][y] + 1
                time_visited[nx][ny] = True
                q.append((nx, ny))

    is_left = False
    # 최대 값
    for i in range(N):
        for j in range(N):
            # 바이러스인 상태
            if board[i][j] == 0:
                # 방문하지 않았다면 바이러스가 제거되지 못한 것
                if not time_visited[i][j]:
                    is_left = True
                    break
                # 방문한 상태라면 최대 값을 구한다. 즉, 바이러스를 제거하는 데 사용된 최대 시간
                else:
                    max_time = max(max_time, steps[i][j])
        if is_left:
            break
    # 각 조합에 대해서 바이러스를 제거하는 최소 시간을 구한다.
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
        # 각 병원들의 조합
        if board[i][j] == 2:
            hospitals.append((i, j))
time = 987654321
candi = [0] * M # 조합에 대한 인덱스 저장
visited = [False] * len(hospitals) # 조합을 구하기 위한 방문 표시
dfs(0, 0)
if time == 987654321:
    time = -1
print(time)