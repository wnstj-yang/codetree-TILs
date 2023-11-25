# 2023-11-25
# 18:00 ~ 19:01


def spread(x, y):
    num = board[x][y] // 5
    if num < 1:
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or board[nx][ny] == -1:
            continue
        # 확산된 위치에 더할 먼지 양과 현재 위치에 먼지 양을 뺀다
        add_board[nx][ny] += num
        board[x][y] -= num


def add():
    for i in range(N):
        for j in range(M):
            board[i][j] += add_board[i][j]


def clean(x, y, direction):
    # 다음을 가리키는 nx, ny 좌표
    nx = x + dx[0]
    ny = y + dy[0]
    number = board[nx][ny] # 움직이면서 넣을 number값 저장
    board[nx][ny] = 0
    # d가 True면 반시계, False면 시계방향 즉, 돌풍의 위와 아래 시작점
    if direction:
        for i in range(4):
            # 각 방향에 맞게 지속적인 좌표 및 현재 먼지의 양을 갱신
            while True:
                next_x = nx + dx[i]
                next_y = ny + dy[i]
                if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
                    break
                if next_x == x and next_y == y:
                    return
                nx, ny = next_x, next_y
                temp = board[nx][ny]
                board[nx][ny] = number
                number = temp

    else:
        for i in range(4):
            d = i
            # d의 변수를 따로 한 것은 우상좌하 -> 우하좌상으로 움직이기 때문에 상, 하를 바꾸기 위해 2를 더해주고 나머지 연산을 통해 진행
            if i == 1 or i == 3:
                d = (d + 2) % 4
            while True:
                next_x = nx + dx[d]
                next_y = ny + dy[d]
                if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
                    break
                if next_x == x and next_y == y:
                    return
                nx, ny = next_x, next_y
                temp = board[nx][ny]
                board[nx][ny] = number
                number = temp


N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
wind = [] # 돌풍의 위치
# 우상좌하
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
# 돌풍의 위치를 각각 구한다 - 돌풍 청소를 위함
for i in range(N):
    for j in range(M):
        if board[i][j] == -1:
            wind.append((i, j))

while T:
    add_board = [[0] * M for _ in range(N)] # 초 당 먼지 확산
    # 각 위치에 먼지가 존재하면 확산 진행
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                spread(i, j)
    add() # 확산된 먼지를 더해준다

    # 돌풍의 위치 2개에서 각각 다른 방향으로 설정
    # d가 True면 반시계, False면 시계방향 즉, 돌풍의 위와 아래 시작점
    clean(wind[0][0], wind[0][1], True)
    clean(wind[1][0], wind[1][1], False)
    T -= 1

total = 0
for i in range(N):
    for j in range(M):
        if board[i][j]:
            total += board[i][j]
# 돌풍 2개
print(total + 2)