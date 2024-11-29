def is_range(x, y):
    if x < 0 or x >= 4 or y < 0 or y >= 4:
        return False
    return True

def move(cx, cy, copy_board):
    for n in range(1, 17):
        is_moved = False
        for x in range(4):
            for y in range(4):
                if len(copy_board[x][y]) > 0 and n == copy_board[x][y][0]:
                    num, d = copy_board[x][y]
                    for k in range(8):
                        nd = (d + k) % 8
                        nx = x + dx[nd]
                        ny = y + dy[nd]
                        # 범위를 벗어나지 않았고
                        if is_range(nx, ny):
                            # 술래말이면 못움직임
                            if cx == nx and cy == ny:
                                continue
                            copy_board[x][y] = [num, nd]
                            copy_board[x][y], copy_board[nx][ny] = copy_board[nx][ny], copy_board[x][y]
                            is_moved = True
                            break
                if is_moved:
                    break
            if is_moved:
                break
    return copy_board

def dfs(x, y, cnt, board):
    global total
    
    copy_board = [[item[:] for item in board[i]] for i in range(4)]
    num, d = copy_board[x][y]
    cnt += num
    total = max(total, cnt)
    copy_board[x][y] = []
    copy_board = move(x, y, copy_board)
    for i in range(1, 5):
        nx = x + dx[d] * i
        ny = y + dy[d] * i
        if is_range(nx, ny) and len(copy_board[nx][ny]) > 0:
            dfs(nx, ny, cnt, copy_board)


board = [[0] * 4 for _ in range(4)]
# 위쪽부터 반시계 방향으로 45도씩 8개 방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
cx, cy = 0, 0
total = 0
for i in range(4):
    info = list(map(int, input().split()))
    for j in range(4):
        num, d = info[j * 2], info[j * 2 + 1] - 1
        board[i][j] = [num, d]

dfs(0, 0, 0, board)
print(total)
