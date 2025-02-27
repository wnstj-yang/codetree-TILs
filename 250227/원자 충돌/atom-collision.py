def move_atomics():
    next_board = [[[] for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if len(board[x][y]) > 0:
                for m, s, d in board[x][y]:
                    # 자신의 방향에 속도만큼 이동
                    nx = (x + dx[d] * s) % N
                    ny = (y + dy[d] * s) % N
                    next_board[nx][ny].append([m, s, d])
    return next_board

def seperate():
    for x in range(N):
        for y in range(N):
            if len(board[x][y]) >= 2:
                m_total, s_total = 0, 0
                is_odd = False
                is_even = False
                for m, s, d in board[x][y]:
                    m_total += m
                    s_total += s
                    # 상하좌우
                    if d % 2:
                        is_odd = True
                    else:
                        is_even = True
                m_val = m_total // 5
                s_val = s_total // len(board[x][y])
                board[x][y] = []
                if m_val == 0:
                    continue
                direcs = [0, 2, 4, 6]
                # 대각선도 있고 상하좌우도 있으면 대각선의 네방향을 가진다. 그 반대는 상하좌우를 가진다
                if is_odd and is_even:
                    direcs = [1, 3, 5, 7]
                for d in direcs:
                    board[x][y].append([m_val, s_val, d])

N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
# 방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(M):
    x, y, m, s, d = map(int, input().split())
    # 질량, 방향, 속력
    board[x - 1][y - 1].append([m, s, d])

for _ in range(K):
    board = move_atomics()
    seperate()

result = 0
for x in range(N):
    for y in range(N):
        if len(board[x][y]) > 0:
            for m, s, d in board[x][y]:
                result += m
print(result)
