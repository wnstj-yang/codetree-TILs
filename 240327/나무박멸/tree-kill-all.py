# 2024-03-27


# 범위 체크
def is_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


# 1. 인접 나무 성장
def grow_trees():
    for x in range(N):
        for y in range(N):
            if board[x][y] > 0:
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if is_range(nx, ny) and board[nx][ny] > 0:
                        board[x][y] += 1


# 2. 인접 나무 번식
def spread_trees():
    next_board = [item[:] for item in board]
    for x in range(N):
        for y in range(N):
            if board[x][y] > 0:
                empty_list = []
                cnt = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if is_range(nx, ny) and toxic[nx][ny] == 0 and board[nx][ny] == 0:
                        empty_list.append((nx, ny))
                        cnt += 1
                if cnt > 0:
                    tree = board[x][y] // cnt
                    for i, j in empty_list:
                        next_board[i][j] += tree
    return next_board


# 3-2. 제초제 뿌릴 시 가장 많이 박멸되는 위치 찾기
def calculate(x, y):
    toxic_list = [(x, y)]
    cnt = 0
    for k in range(4, 8):
        for l in range(1, K + 1):
            nx = x + dx[k] * l
            ny = y + dy[k] * l
            # 범위를 벗어나거나 벽을 만나면 해당 위치에는 제초제 X
            if not is_range(nx, ny) or board[nx][ny] == -1:
                break
            # 나무 개수가 0이상일 때 개수를 더해주고 제초제 위치를 넣어준다
            if board[nx][ny] >= 0:
                cnt += board[nx][ny]
                toxic_list.append((nx, ny))
                # 다만, 0인 경우에는 해당 부분까지만 제초제를 뿌리고 그 이상 넘어가지는 않는다.
                if board[nx][ny] == 0:
                    break
    return [cnt, toxic_list]


# 3-1. 제초제 위치를 찾고 심어주기
def spread_toxic():
    max_cnt = -1
    max_list = []

    for x in range(N):
        for y in range(N):
            if board[x][y] > 0:
                cnt, toxic_list = calculate(x, y)
                cnt += board[x][y]
                if cnt > max_cnt:
                    max_list = toxic_list
                    max_cnt = cnt

    # 제초제를 심어주고
    for x, y in max_list:
        toxic[x][y] = C + 1
        board[x][y] = 0
    if max_cnt == -1:
        max_cnt = 0
    return max_cnt


# 4. 제초제 유지 기간 감소
def decrease_toxic():
    for x in range(N):
        for y in range(N):
            if toxic[x][y]:
                toxic[x][y] -= 1


N, M, K, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
toxic = [[0] * N for _ in range(N)]
# 상하좌우 + 좌상 우상 우하 좌하 대각선
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]
result = 0
for _ in range(M):
    grow_trees()
    board = spread_trees()
    result += spread_toxic()
    decrease_toxic()
print(result)