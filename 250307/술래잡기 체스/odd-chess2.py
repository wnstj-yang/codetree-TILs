def is_range(x, y):
    if x < 0 or x >= 4 or y < 0 or y >= 4:
        return False
    return True


def move(cx, cy, copy_board):
    for num in range(1, 17):
        is_moved = False
        for x in range(4):
            for y in range(4):
                if len(copy_board[x][y]) > 0 and copy_board[x][y][0] == num:
                    d = copy_board[x][y][1]
                    for k in range(8):
                        nd = (d + k) % 8
                        nx = x + dx[nd]
                        ny = y + dy[nd]
                        if is_range(nx, ny):
                            # 술래말이랑 같은 곳이 된다면 넘어간다
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
# dfs 필요
def catch(x, y, cnt, arr):
    global total

    copy_board = [[item[:] for item in arr[i]] for i in range(4)]

    cnt += copy_board[x][y][0]
    total = max(total, cnt)
    d = copy_board[x][y][1]

    copy_board[x][y] = []
    copy_board = move(x, y, copy_board)
    for i in range(1, 4):
        nx = x + dx[d] * i
        ny = y + dy[d] * i
        if is_range(nx, ny) and len(copy_board[nx][ny]) > 0:
            catch(nx, ny, cnt, copy_board)



# 위에서부터 반시계 8방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
board = [[[] for _ in range(4)] for _ in range(4)]
total = 0
for i in range(4):
    info_list = list(map(int, input().split()))
    for j in range(4):
        num, d = info_list[j * 2], info_list[j * 2 + 1]
        board[i][j] = [num, d - 1]
catch(0, 0, 0, board)
print(total)
