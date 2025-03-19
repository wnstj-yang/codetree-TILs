def move_nutrition(d, p):
    next_nutritional = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if nutritional_board[i][j]:
                x = (i + dx[d] * p) % N
                y = (j + dy[d] * p) % N
                next_nutritional[x][y] = True
    return next_nutritional


def set_nutrition():
    for i in range(N):
        for j in range(N):
            if nutritional_board[i][j]:
                board[i][j] += 1

def grow_trees():
    for x in range(N):
        for y in range(N):
            if nutritional_board[x][y]:
                cnt = 0
                for k in [1, 3, 5, 7]:
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if board[nx][ny] > 0:
                        cnt += 1
                board[x][y] += cnt

def cut_supply():
    for x in range(N):
        for y in range(N):
            if board[x][y] >= 2 and not nutritional_board[x][y]:
                board[x][y] -= 2
                nutritional_board[x][y] = True
            else:
                nutritional_board[x][y] = False


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# 문제 순서에 맞는 8 방향
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
nutritional_board = [[False] * N for _ in range(N)]
for i in range(N - 1, N - 3, -1):
    for j in range(2):
        nutritional_board[i][j] = True
# 1. 특수 영양제 이동
for _ in range(M):
    d, p = map(int, input().split())
    d -= 1
    nutritional_board = move_nutrition(d, p) # 특수 영양제 이동
    set_nutrition() # 특수 영양제 투입
    grow_trees() # 대각선 인접 리브로수 추가
    cut_supply() # 높이 2이상 잘라내고 영양제 올려준다

total = 0
for b in board:
    total += sum(b)
print(total)
