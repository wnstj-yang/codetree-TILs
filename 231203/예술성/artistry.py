# 2023-12-03
# 21:35 ~ 23:00


from collections import deque


# group 좌표들 구하기
def get_group(x, y):
    group = [(x, y)]
    q = deque()
    q.append((x, y))
    number = board[x][y]
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            # 같은 숫자이고 방문하지 않은 곳이여야 한다.
            if not visited[nx][ny] and board[nx][ny] == number:
                visited[nx][ny] = True
                group.append((nx, ny))
                q.append((nx, ny))
    return group


# 경계선의 개수를 구하기
def get_borders(coors, target):
    cnt = 0
    target_num = board[target[0][0]][target[0][1]]
    for x, y in coors:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            # 숫자를 파악하고 좌표 값이 target에 존재하는지 확인
            # 4방향을 파악하기 때문에 다른 숫자도 볼 수 있어서 숫자도 조건에 들어가야 한다.
            if board[nx][ny] == target_num and (nx, ny) in target:
                cnt += 1
    return cnt


def pair_group(idx, cnt):
    global result

    if cnt == 2:
        first, second = groups[candi[0]], groups[candi[1]]
        border = get_borders(first, second)
        fx, fy = first[0][0], first[0][1]
        sx, sy = second[0][0], second[0][1]
        calculate = (len(first) + len(second)) * board[fx][fy] * board[sx][sy] * border
        result += calculate
        return

    for i in range(idx, len(groups)):
        candi[cnt] = i
        pair_group(i + 1, cnt + 1)


def rotate():
    next_board = [[0] * N for _ in range(N)]
    # 1. 십자 모양으로 반시계 진행
    for idx in range(N):
        next_board[N // 2][idx] = board[idx][N // 2]
        next_board[N - 1 - idx][N // 2] = board[N // 2][idx]

    # 2. 이외 부분 돌리기
    # 왼쪽 위
    for i in range(N // 2):
        for j in range(N // 2):
            next_board[j][N // 2 - 1 - i] = board[i][j]

    # 오른쪽 위
    for i in range(N // 2):
        for j in range(N // 2 + 1, N):
            next_board[j - 1 - N // 2][N - 1 - i] = board[i][j]

    # 왼쪽 아래
    for i in range(N // 2 + 1, N):
        for j in range(N // 2):
            next_board[N // 2 + 1 + j][N - 1 - i] = board[i][j]

    # 오른쪽 아래
    idx = 0
    for i in range(N // 2 + 1, N):
        for j in range(N // 2 + 1, N):
            next_board[j][N - 1 - idx] = board[i][j]
        idx += 1

    return next_board


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
groups = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
candi = [0] * 2
total = 0
for _ in range(4):
    visited = [[False] * N for _ in range(N)]
    groups = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                groups.append(get_group(i, j))
    result = 0
    pair_group(0, 0)
    total += result
    board = rotate()

print(total)