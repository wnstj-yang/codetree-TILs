from collections import deque

def is_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True

# 중앙에서부터 시작해서 달팽이 모양으로 숫자들을 땡겨서 저장한다.
def set_monsters():
    length = 1
    length_cnt = 0
    cnt = 2
    coor_list = []
    sx, sy = N // 2, N // 2
    sd = 2
    while length < N:
        nx = sx + dx[sd]
        ny = sy + dy[sd]
        if board[nx][ny]:
            coor_list.append(board[nx][ny])
        length_cnt += 1
        if length == length_cnt:
            length_cnt = 0
            cnt -= 1
            sd = (sd - 1) % 4
            if cnt == 0:
                length += 1
                if length == N - 1:
                    cnt = 3
                else:
                    cnt = 2
        sx, sy = nx, ny

    length = 1
    length_cnt = 0
    cnt = 2
    sx, sy = N // 2, N // 2
    sd = 2
    idx = 0
    next_board = [[0] * N for _ in range(N)]
    while length < N:
        nx = sx + dx[sd]
        ny = sy + dy[sd]
        if idx < len(coor_list):
            next_board[nx][ny] = coor_list[idx]
            idx += 1
        else:
            break
        length_cnt += 1
        if length == length_cnt:
            length_cnt = 0
            cnt -= 1
            sd = (sd - 1) % 4
            if cnt == 0:
                length += 1
                if length == N - 1:
                    cnt = 3
                else:
                    cnt = 2
        sx, sy = nx, ny
    return next_board


def check_duplicate():
    length = 1
    length_cnt = 0
    cnt = 2
    sx, sy = N // 2, N // 2
    sd = 2
    prev = board[sx][sy]
    val_cnt = 0
    delete_list = {}
    duplicate = []
    while length < N:
        nx = sx + dx[sd]
        ny = sy + dy[sd]
        if prev == board[nx][ny] and board[nx][ny] > 0:
            val_cnt += 1
            duplicate.append((nx, ny))
        else:
            if val_cnt >= 4:
                # !!! 겹칠 수가 있으니 주의
                if prev in delete_list:
                    delete_list[prev].extend(duplicate)
                else:
                    delete_list[prev] = duplicate
            val_cnt = 1
            prev = board[nx][ny]
            duplicate = [(nx, ny)]

        length_cnt += 1
        if length == length_cnt:
            length_cnt = 0
            cnt -= 1
            sd = (sd - 1) % 4
            if cnt == 0:
                length += 1
                if length == N - 1:
                    cnt = 3
                else:
                    cnt = 2
        sx, sy = nx, ny
    return delete_list


def set_new_board():
    length = 1
    length_cnt = 0
    cnt = 2
    sx, sy = N // 2, N // 2
    sd = 2
    prev = board[sx][sy]
    val_cnt = 0
    set_list = []
    while length < N:
        nx = sx + dx[sd]
        ny = sy + dy[sd]
        if prev == board[nx][ny] and board[nx][ny] > 0:
            val_cnt += 1
        else:
            if prev > 0:
                set_list.append(val_cnt)
                set_list.append(prev)
            val_cnt = 1
            prev = board[nx][ny]

        length_cnt += 1
        if length == length_cnt:
            length_cnt = 0
            cnt -= 1
            sd = (sd - 1) % 4
            if cnt == 0:
                length += 1
                if length == N - 1:
                    cnt = 3
                else:
                    cnt = 2
        sx, sy = nx, ny
    length = 1
    length_cnt = 0
    cnt = 2
    sx, sy = N // 2, N // 2
    sd = 2
    idx = 0
    next_board = [[0] * N for _ in range(N)]
    while length < N:
        nx = sx + dx[sd]
        ny = sy + dy[sd]
        if idx < len(set_list):
            next_board[nx][ny] = set_list[idx]
            idx += 1
        else:
            break
        length_cnt += 1
        if length == length_cnt:
            length_cnt = 0
            cnt -= 1
            sd = (sd - 1) % 4
            if cnt == 0:
                length += 1
                if length == N - 1:
                    cnt = 3
                else:
                    cnt = 2
        sx, sy = nx, ny
    return next_board
# 우하좌상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
total = 0
cd = 2
cx, cy = N // 2, N // 2
for _ in range(M):
    d, p = map(int, input().split())
    # 1. 공격
    for i in range(1, p + 1):
        nx = cx + dx[d] * i
        ny = cy + dy[d] * i
        if is_range(nx, ny):
            total += board[nx][ny]
            board[nx][ny] = 0
        else:
            break
    board = set_monsters()
    while True:
        delete_list = check_duplicate()
        if len(delete_list) == 0:
            break
        else:
            for val, coors in delete_list.items():
                total += (val * len(coors))
                for x, y in coors:
                    board[x][y] = 0
            board = set_monsters()
    board = set_new_board()

print(total)

