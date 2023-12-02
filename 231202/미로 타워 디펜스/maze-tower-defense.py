# 2023-12-02
# 14:20 ~ 16:20
# 예외 처리에 대한 중복 코드가 늘어나는 데 추후 합쳐서 정리해야할 듯 하다.

from collections import deque


def attack(d, p):
    global total
    
    # 중앙의 플레이어 위치에서 p만큼 값을 없애고 없앤 값은 결과값에 더해준다. 범위를 나가면 끝
    for i in range(1, p + 1):
        nx = sx + dx[d] * i
        ny = sy + dy[d] * i
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            return
        total += board[nx][ny]
        board[nx][ny] = 0


# 아래의 채우는 로직 내에 달팽이처럼 살펴보는 것은 다른 함수에서도 동일하기에 해당 부분에서만 주석
def fill():
    length = 1 # 길이만큼 움직이고 꺾이는 부분이 존재한다
    cnt = 2 # 길이가 N - 1 제외하고는 length만큼 2번 꺾는다
    direc = 0 # 방향
    x, y = N // 2, N // 2 # 중앙에서 시작
    empty = deque()
    while True:
        for _ in range(length):
            nx = x + dx[direc]
            ny = y + dy[direc]
            # 0이면 비어있으므로 리스트에 좌표 값 추가
            if board[nx][ny] == 0:
                empty.append((nx, ny))
            else:
                # 현재 위치가 0보다 크고 기존에 빈 공간이 있다면 현재 값으로 채워넣고 0으로 초기화, 빈 공간에 좌표 추가를 진행
                if empty:
                    ex, ey = empty.popleft()
                    board[ex][ey] = board[nx][ny]
                    board[nx][ny] = 0
                    empty.append((nx, ny))
            x, y = nx, ny
        # 첫 번째 위치 즉, 달팽의 순회의 끝에 오면 끝
        if x == 0 and y == 0:
            return
        
        # cnt를 줄여나가며 방향과 꺾는 부분을 갱신
        cnt -= 1
        direc = (direc + 1) % 4
        # length의 길이로 cnt만큼 꺾었으면 length증가 및 cnt 초기화
        if cnt == 0:
            length += 1
            cnt = 2
            # 달팽의 순회의 마지막 길이가 N - 1이고, 마지막 길이면 3번 꺾기에 cnt = 3으로 초기화
            if length == N - 1:
                cnt = 3


def delete():
    global total

    length = 1
    cnt = 2
    direc = 0
    x, y = N // 2, N // 2
    same = deque((x, y))
    same_cnt = 1
    value = board[x][y]
    deleted = False
    while True:
        for _ in range(length):
            nx = x + dx[direc]
            ny = y + dy[direc]
            # 빈 공간 없이 채워져서 순회하므로 비어있다면 끝
            if board[nx][ny] == 0:
                if same_cnt >= 4:
                    deleted = True
                    for i, j in same:
                        total += board[i][j]
                        board[i][j] = 0
                return deleted

            # 같은 값이라면 개수 증가 및 좌표 추가
            if board[nx][ny] == value:
                same_cnt += 1
                same.append((nx, ny))
            else:
                if same_cnt >= 4:
                    deleted = True
                    for i, j in same:
                        total += board[i][j]
                        board[i][j] = 0
                same_cnt = 1
                same = [(nx, ny)]
                value = board[nx][ny]
            x, y = nx, ny

        if x == 0 and y == 0:
            if same_cnt >= 4:
                deleted = True
                for i, j in same:
                    board[i][j] = 0
            return deleted

        cnt -= 1
        direc = (direc + 1) % 4
        if cnt == 0:
            length += 1
            cnt = 2
            if length == N - 1:
                cnt = 3


def fill_pairs():
    next_board = [[0] * N for _ in range(N)]
    length = 1
    cnt = 2
    direc = 0
    x, y = N // 2, N // 2
    pairs = deque()
    same_cnt = 0
    value = 0
    is_end = False
    while True:
        for _ in range(length):
            nx = x + dx[direc]
            ny = y + dy[direc]
            if board[nx][ny] == 0:
                is_end = True
                break
            if board[nx][ny] == value:
                same_cnt += 1
            else:
                # 시작점부터 시작하기 때문에 해당 부분은 포함시키지 않는다.
                if same_cnt != 0:
                    pairs.extend([same_cnt, value])
                value = board[nx][ny]
                same_cnt = 1
            x, y = nx, ny
        if is_end or (x == 0 and y == 0):
            pairs.extend([same_cnt, value])
            break

        cnt -= 1
        direc = (direc + 1) % 4
        if cnt == 0:
            length += 1
            cnt = 2
            if length == N - 1:
                cnt = 3

    #  짝지어진 것을 다시 채워준다
    x, y = N // 2, N // 2
    length = 1
    cnt = 2
    direc = 0
    while True:
        for _ in range(length):
            nx = x + dx[direc]
            ny = y + dy[direc]
            if pairs:
                next_board[nx][ny] = pairs.popleft()
            else:
                return next_board
            x, y = nx, ny
        if x == 0 and y == 0:
            return next_board

        cnt -= 1
        direc = (direc + 1) % 4
        if cnt == 0:
            length += 1
            cnt = 2
            if length == N - 1:
                cnt = 3


# 좌하우상
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
sx, sy = N // 2, N // 2
total = 0
for _ in range(M):
    d, p = map(int, input().split())
    if d == 0 or d == 2:
        d = (d + 2) % 4
    attack(d, p)
    fill()
    while True:
        if not delete():
            break
        fill()
    board = fill_pairs()
print(total)