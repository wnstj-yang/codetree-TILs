# 2024-03-23


def is_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


def attack(d, p):
    global result

    x, y = N // 2, N // 2
    for _ in range(p):
        x = x + dx[d]
        y = y + dy[d]
        if is_range(x, y):
            result += board[x][y]
            board[x][y] = 0


# 2. 몬스터들을 찾고 다시 채워준다
def fill_monsters():
    step = 1
    limit = 2
    step_cnt = 0
    limit_cnt = 0
    d = 2
    x, y = N // 2, N // 2
    monster_list = []
    while True:
        if x == 0 and y == 0:
            break
        nx = x + dx[d]
        ny = y + dy[d]
        step_cnt += 1
        if step_cnt == step:
            d = (d - 1) % 4
            step_cnt = 0
            limit_cnt += 1
            if limit_cnt == limit:
                limit_cnt = 0
                step += 1
                if step == N - 1: # 마지막은 3번 진행해야됨
                    limit = 3
        if board[nx][ny]:
            monster_list.append(board[nx][ny])
        x, y = nx, ny # 좌표 갱신

    step = 1
    limit = 2
    step_cnt = 0
    limit_cnt = 0
    d = 2
    x, y = N // 2, N // 2
    temp = [[0] * N for _ in range(N)]
    idx = 0
    length = len(monster_list)
    while True:
        if idx >= length:
            break
        if x == 0 and y == 0:
            break
        nx = x + dx[d]
        ny = y + dy[d]
        step_cnt += 1
        if step_cnt == step:
            d = (d - 1) % 4
            step_cnt = 0
            limit_cnt += 1
            if limit_cnt == limit:
                limit_cnt = 0
                step += 1
                if step == N - 1: # 마지막은 3번 진행해야됨
                    limit = 3
        temp[nx][ny] = monster_list[idx]
        idx += 1
        x, y = nx, ny
    return temp


def remove_monsters():
    global result

    step = 1
    limit = 2
    step_cnt = 0
    limit_cnt = 0
    d = 2
    x, y = N // 2, N // 2
    target = 0
    target_cnt = 0
    target_list = []
    is_removed = False

    while True:
        if x == 0 and y == 0:
            break
        nx = x + dx[d]
        ny = y + dy[d]
        step_cnt += 1
        if step_cnt == step:
            d = (d - 1) % 4
            step_cnt = 0
            limit_cnt += 1
            if limit_cnt == limit:
                limit_cnt = 0
                step += 1
                if step == N - 1: # 마지막은 3번 진행해야됨
                    limit = 3
        if target == board[nx][ny] and board[nx][ny] != 0:
            target_cnt += 1
            target_list.append((nx, ny))
        else:
            if target_cnt >= 4:
                is_removed = True
                for i, j in target_list:
                    board[i][j] = 0
                result += (target_cnt * target)
            target = board[nx][ny]
            target_cnt = 1
            target_list = [(nx, ny)]
        x, y = nx, ny # 좌표 갱신

    return is_removed


def fill_pair():
    step = 1
    limit = 2
    step_cnt = 0
    limit_cnt = 0
    d = 2
    x, y = N // 2, N // 2
    target = 0
    target_cnt = 0
    fill_list = []
    while True:
        if x == 0 and y == 0:
            break
        nx = x + dx[d]
        ny = y + dy[d]
        step_cnt += 1
        if step_cnt == step:
            d = (d - 1) % 4
            step_cnt = 0
            limit_cnt += 1
            if limit_cnt == limit:
                limit_cnt = 0
                step += 1
                if step == N - 1: # 마지막은 3번 진행해야됨
                    limit = 3
        if target == board[nx][ny] and board[nx][ny] != 0:
            target_cnt += 1
        else:
            if target != 0:
                fill_list.extend([target_cnt, target])
            target = board[nx][ny]
            target_cnt = 1
        x, y = nx, ny # 좌표 갱신

    step = 1
    limit = 2
    step_cnt = 0
    limit_cnt = 0
    d = 2
    x, y = N // 2, N // 2
    temp = [[0] * N for _ in range(N)]
    idx = 0
    length = len(fill_list)
    while True:
        if idx >= length:
            break
        if x == 0 and y == 0:
            break
        nx = x + dx[d]
        ny = y + dy[d]
        step_cnt += 1
        if step_cnt == step:
            d = (d - 1) % 4
            step_cnt = 0
            limit_cnt += 1
            if limit_cnt == limit:
                limit_cnt = 0
                step += 1
                if step == N - 1: # 마지막은 3번 진행해야됨
                    limit = 3
        temp[nx][ny] = fill_list[idx]
        idx += 1
        x, y = nx, ny
    return temp


# 우하좌상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, M = map(int, input().split())
attacks = []
board = [list(map(int, input().split())) for _ in range(N)]
result = 0
for _ in range(M):
    d, p = map(int, input().split())
    attack(d, p)
    board = fill_monsters()
    while remove_monsters():
        board = fill_monsters()
    board = fill_pair()

print(result)