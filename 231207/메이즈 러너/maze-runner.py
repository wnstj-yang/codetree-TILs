# 2023-12-05 ~ 2023-12-06

def move():
    global total

    moved = [[[] for _ in range(N)] for _ in range(N)]

    # 최단 거리를 구하고 4방향 움직였을 때 이거 보다 작다면 움직이기 가능
    for i in range(N):
        for j in range(N):
            # 플레이어가 존재하면 움직여준다
            if len(players[i][j]) > 0:
                min_dist = abs(i - ex) + abs(j - ey)
                for p in players[i][j]:
                    is_moved = False
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue
                        dist = abs(nx - ex) + abs(ny - ey)
                        # 출구 나가면 끝. 즉, 진또배기 최단거리임
                        if dist == 0:
                            total += 1
                            is_moved = True
                            check_player[p] = 0
                            break
                        # 빈 공간에 최단 거리가 가깝다면 우선순위에 따라 발견되면 움직인다.
                        # 2개 이상이 아니더라도 거리가 최단거리보다 작으면 4방향 중 가장 가깝다는 의미이기에 조건문에 포함되어 판단한다
                        if board[nx][ny] == 0 and dist < min_dist:
                            moved[nx][ny].append(p)
                            total += 1
                            is_moved = True
                            break

                    if not is_moved:
                        moved[i][j].append(p)
    return moved


def get_square():
    # l : 정사각형의 길이, i, j : 행,열 시작점
    for l in range(2, N):
        for i in range(N - l + 1):
            for j in range(N - l + 1):
                is_people = False
                is_exit = False
                # x, y : 행, 열 시작점으로부터 각 정사각형 길이인 l길이만큼 안의 값 순회
                for x in range(i, i + l):
                    for y in range(j, j + l):
                        if len(players[x][y]) > 0:
                            is_people = True
                        if x == ex and y == ey:
                            is_exit = True
                        if is_people and is_exit:
                            return [l, i, j]
    return [0, 0, 0]


def rotate(length, x, y):
    global ex, ey
    # 일부분에 있는 거를 회전 시켜야한다.
    # 탈출구 갱신
    mid_board = [[0] * N for _ in range(N)]
    next_board = [[0] * N for _ in range(N)]
    mid_players = [[[] for _ in range(N)] for _ in range(N)]
    next_players = [[[] for _ in range(N)] for _ in range(N)]
    # 1. 값 회전을 수월하게 하기 위해 정사각형에 있는 회전 값들의 시작을 0,0 으로 옮긴다.
    for i in range(x, x + length):
        for j in range(y, y + length):
            mid_board[i - x][j - y] = board[i][j]
            mid_players[i - x][j - y] = players[i][j]

    # 2. 0,0에서부터 시작하여 회전을 진행한다.
    for i in range(length):
        for j in range(length):
            next_board[j][length - 1 - i] = mid_board[i][j]
            next_players[j][length - 1 - i] = mid_players[i][j]

    # 3. 기존 격자판, 참가자들의 값에 넣어준다 + 벽 내구도 줄이기
    for i in range(x, x + length):
        for j in range(y, y + length):
            board[i][j] = next_board[i - x][j - y]
            players[i][j] = next_players[i - x][j - y]
            if board[i][j] == 10:
                ex = i
                ey = j
                continue
            board[i][j] -= 1
            if board[i][j] < 0:
                board[i][j] = 0


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
players = [[[] for _ in range(N)] for _ in range(N)]
check_player = {}
total = 0
for i in range(1, M + 1):
    x, y = map(int, input().split())
    players[x - 1][y - 1].append(i)
    check_player[i] = 1 # player번호에 맞게 존재하는 것으로 판단
ex, ey = map(int, input().split())
ex -= 1
ey -= 1
board[ex][ey] = 10 # 탈출구
for i in range(K):
    # 플레이어의 값들의 합이 0이면
    if sum(check_player.values()) == 0:
        break
    players = move() # 1. 플레이어들의 이동
    l, x, y = get_square() # l : 정사각형 길이, x : 행, y : 열
    if l + x + y == 0: # 각 합이 0이면 가장 작은 정사각형이 없다는 의미이다.
        continue
    rotate(l, x, y)
print(total)
print(ex + 1, ey + 1)