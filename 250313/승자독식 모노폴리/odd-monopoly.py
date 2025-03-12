def is_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


def move():
    next_board = [item[:] for item in board]
    next_players = {}
    for key, value in players.items():
        x, y = value
        if len(board[x][y]) > 0:
            num, d, cnt = board[x][y]
            is_moved = False
            for nd in players_directions[num][d]:
                nx = x + dx[nd]
                ny = y + dy[nd]
                if is_range(nx, ny):
                    if len(board[nx][ny]) == 0:
                        # 한 공간에 겹치는 경우 숫자가 작은 것이 남는다.
                        if new_occupy[nx][ny] and next_board[nx][ny][0] < num:
                            is_moved = True
                            break
                        next_players[num] = [nx, ny]
                        next_board[nx][ny] = [num, nd, K]
                        new_occupy[nx][ny] = True
                        is_moved = True
                        break

            if not is_moved:
                # print(players_directions)
                for nd in players_directions[num][d]:
                    nx = x + nd
                    ny = y + nd
                    if is_range(nx, ny) and len(board[nx][ny]) > 0 and board[nx][ny][0] == num:
                        next_players[num] = [nx, ny]
                        next_board[nx][ny] = [num, nd, K]
                        new_occupy[nx][ny] = True
                        break
    # for num in remove_players:
    #     del players[num]
    return next_players, next_board


def remove_occupy():
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) > 0 and not new_occupy[i][j]:
                board[i][j][2] -= 1
                if board[i][j][2] <= 0:
                    board[i][j] = []



N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
first_directions = list(map(int, input().split()))
players_directions = {}
players = {}
# 상하좌우
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if board[i][j] > 0:
            players[board[i][j]] = [i, j]
            board[i][j] = [board[i][j], first_directions[board[i][j] - 1], K]
        else:
            board[i][j] = []

for i in range(M):
    players_directions[i + 1] = {}
    for j in range(M):
        players_directions[i + 1][j + 1] = list(map(int, input().split()))

turn = 1
while turn <= 1000:
    new_occupy = [[False] * N for _ in range(N)]
    players, board = move()
    remove_occupy()
    if len(players) == 1:
        keys = list(players.keys())
        if keys[0] == 1:
            break
    # print(turn)
    # for z in board:
    #     print(z)
    # print()
    turn += 1
if turn >= 1001:
    print(-1)
else:
    print(turn)
