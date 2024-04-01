# 2024-04-01


def is_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


# 1. 도망자 움직이기
def move_runners():
    next_board = [[[] for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if len(board[x][y]) > 0:
                for d in board[x][y]:
                    dist = abs(cx - x) + abs(cy - y)
                    if dist > 3:
                        next_board[x][y].append(d)
                        continue
                    nx = x + dx[d]
                    ny = y + dy[d]
                    # 범위를 벗어나면 방향을 바꿔주고 이동해보기
                    if not is_range(nx, ny):
                        d = (d + 2) % 4
                        nx = x + dx[d]
                        ny = y + dy[d]
                    # 술래가 존재하면 그 자리에 방향 추가 아니라면 이동
                    if nx == cx and ny == cy:
                        next_board[x][y].append(d)
                    else:
                        next_board[nx][ny].append(d)
    return next_board


# 2. 술래 이동
# length = 1 # 술래가 움직여야하는 길이
# cnt_length = 0 # 술래가 움직여야하는 길이 카운트
# limit_cnt = 2 # 술래가 길이를 몇 번 움직이는지 제한
# cnt = 0 # 술래가 길이 몇 번 움직였는지 체크
# c_d = 0 # 술래의 방향
# way = True # True면 처음 위 방향으로 False면 중앙으로
def move_catcher(turn):
    global length, cnt_length, limit_cnt, cnt, c_d, way, cx, cy

    cnt_length += 1
    cx = cx + dx[c_d]
    cy = cy + dy[c_d]
    if cnt_length == length:
        cnt_length = 0
        cnt += 1
        if way:
            c_d = (c_d + 1) % 4
            if cnt == limit_cnt:
                length += 1
                cnt = 0
                if length == N - 1:
                    limit_cnt = 3
                if cx == 0 and cy == 0:
                    way = False
                    length = N - 1
                    c_d = 2
        else:
            c_d = (c_d - 1) % 4
            if cnt == limit_cnt:
                if length == N - 1:
                    limit_cnt = 2
                length -= 1
                cnt = 0
                if cx == N // 2 and cy == N // 2:
                    way = True
                    length = 1
                    c_d = 0
    runner_cnt = 0
    for i in range(3):
        nx = cx + dx[c_d] * i
        ny = cy + dy[c_d] * i
        if is_range(nx, ny) and not trees[nx][ny]:
            if len(board[nx][ny]) > 0:
                runner_cnt += turn * len(board[nx][ny])
                board[nx][ny] = []
    return runner_cnt


N, M, H, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
trees = [[False] * N for _ in range(N)]
# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cx, cy = N // 2, N // 2 # 술래 위치
length = 1 # 술래가 움직여야하는 길이
cnt_length = 0 # 술래가 움직여야하는 길이 카운트
limit_cnt = 2 # 술래가 길이를 몇 번 움직이는지 제한
cnt = 0 # 술래가 길이 몇 번 움직였는지 체크
c_d = 0 # 술래의 방향
way = True # True면 처음 위 방향으로 False면 중앙으로
result = 0
for _ in range(M):
    x, y, d = map(int, input().split())
    if d == 1:
        board[x - 1][y - 1].append(1)
    else:
        board[x - 1][y - 1].append(2)
for _ in range(H):
    x, y = map(int, input().split())
    trees[x - 1][y - 1] = True

for turn in range(1, K + 1):
    board = move_runners()
    result += move_catcher(turn)
print(result)