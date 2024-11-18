# 1. 모든 원자의 이동
def move_atomics():
    next_board = [[[] for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if len(board[x][y]) > 0:
                for m, s, d in board[x][y]:
                    nx = (x + dx[d] * s) % N
                    ny = (y + dy[d] * s) % N
                    next_board[nx][ny].append((m, s, d))
    return next_board

# 2. 이동 완료 후 합성 체크
def check():
    for x in range(N):
        for y in range(N):
            if len(board[x][y]) >= 2:
                total_m = 0
                total_s = 0
                is_odd = False
                is_even = False
                for m, s, d in board[x][y]:
                    # 방향들에 대해서 flag값 설정
                    if d % 2:
                        is_odd = True
                    else:
                        is_even = True
                    total_m += m
                    total_s += s
                set_m = total_m // 5
                set_s = total_s // len(board[x][y])
                board[x][y] = [] # 빈 리스트로 초기화
                # 질량 나눈 값이 0이면 비워놓고 끝
                if total_m // 5 == 0:
                    continue
                directions = [0, 2, 4, 6]
                # 둘 다 참이면 대각선을 가진다
                if is_odd and is_even:
                    directions = [1, 3, 5, 7]
                for d in directions:
                    board[x][y].append((set_m, set_s, d))


                    



dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
total = 0
for _ in range(M):
    x, y, m, s, d = map(int, input().split())
    board[x - 1][y - 1].append((m, s, d))

for _ in range(K):
    board = move_atomics()
    check()


for x in range(N):
    for y in range(N):
        if board[x][y]:
            for m, s, d in board[x][y]:
                total += m
print(total)
