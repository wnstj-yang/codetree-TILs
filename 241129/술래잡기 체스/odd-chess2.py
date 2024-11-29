def is_range(x, y):
    if x < 0 or x >= 4 or y < 0 or y >= 4:
        return False
    return True

def move(arr):
    for n in range(1, 17):
        is_moved = False
        for x in range(4):
            for y in range(4):
                if arr[x][y] and n == arr[x][y][0]:
                    num, d = arr[x][y]
                    nd = d
                    for k in range(8):
                        nd = (d + k) % 8
                        nx = x + dx[nd]
                        ny = y + dy[nd]
                        # 범위를 벗어나지 않았고
                        if is_range(nx, ny):
                            # 술래말이면 못움직임
                            if cx == nx and cy == ny:
                                continue
                            # 비어 있는 경우 움직이고 현재 위치 초기화
                            # if len(arr[nx][ny]) == 0:
                            #     arr[nx][ny] = [num, nd]
                            #     arr[x][y] = []
                            #     is_moved = True
                            #     break
                            # 다른 도둑말이 있는 경우 교환
                            # if arr[nx][ny]:
                            arr[x][y] = [num, nd]
                            arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
                            is_moved = True
                            break
                if is_moved:
                    break
            if is_moved:
                break
    return arr

def dfs(x, y, cnt, arr):
    global cx, cy, total
    
    copy_board = [[item[:] for item in arr[i]] for i in range(4)]
    num, d = copy_board[x][y]
    cnt += num
    total = max(total, cnt)
    cx, cy = x, y
    copy_board[x][y] = []
    copy_board = move(copy_board)
    for i in range(1, 5):
        nx = cx + dx[d] * i
        ny = cy + dy[d] * i
        if is_range(nx, ny) and copy_board[nx][ny]:
            dfs(nx, ny, cnt, copy_board)



board = [[0] * 4 for _ in range(4)]
# 위쪽부터 반시계 방향으로 45도씩 8개 방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
cx, cy, cd = 0, 0, 0
total = 0
for i in range(4):
    info = list(map(int, input().split()))
    for j in range(4):
        num, d = info[j * 2], info[j * 2 + 1] - 1
        board[i][j] = [num, d]

dfs(0, 0, 0, board)
print(total)

