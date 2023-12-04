# 2023-12-04
# 21:30 ~

from collections import deque


# 1. 기사 이동
def move_knights(knights, d):
    new_knights = set() # 밀었을 때 움직여야 할 기사들의 번호
    for num in knights: # 움직여야 할 기사들의 번호
        next_knight_coors[num] = []
        for x, y in knight_coors[num]:
            nx = x + dx[d]
            ny = y + dy[d]
            # 범위를 벗어나거나 벽을 만나면 그대로 있는다.
            if nx < 0 or nx >= L or ny < 0 or ny >= L or board[nx][ny] == 2:
                return [-1]
            next_knight_coors[num].append((nx, ny)) # 각 기사의 밀어나졌을 때의 갱신된 좌표 값 추가
            # 상태 격자판에서 0보다 크고 이미 밀어진 기사 번호가 없다면 추가해준다
            if state[nx][ny] > 0 and state[nx][ny] != num:
                new_knights.add(state[nx][ny])
    return list(new_knights)


# 2. 대결 대미지
def fight(num):
    delete_keys = []
    for key, values in knight_coors.items():
        cnt = 0
        if key == num or key not in moved:
            continue
        for x, y in values:
            if board[x][y] == 1:
                cnt += 1
        life[key] -= cnt
        damaged[key] += cnt
        if life[key] <= 0:
            del life[key]
            del damaged[key]
            delete_keys.append(key)
    for k in delete_keys:
        del knight_coors[k]


def update_state():
    next_state = [[0] * L for _ in range(L)]
    for key, values in knight_coors.items():
        for x, y in values:
            next_state[x][y] = key
    return next_state


L, N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(L)]
state = [[0] * L for _ in range(L)]
# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
life = {}
damaged = {}
knight_coors = {}
total = 0
for i in range(1, N + 1):
    r, c, h, w, k = map(int, input().split())
    life[i] = k
    damaged[i] = 0
    r -= 1
    c -= 1
    knight_coors[i] = []
    for x in range(r, r + h):
        for y in range(c, c + w):
            state[x][y] = i
            knight_coors[i].append((x, y))

for z in range(Q):
    i, d = map(int, input().split())
    if i not in life:
        continue
    knights = [i]
    next_knight_coors = {}
    moved = []
    is_move = True
    while True:
        knights = move_knights(knights, d)
        moved.extend(knights)
        if len(knights) == 0:
            break
        elif knights[0] == -1:
            is_move = False
            break
    if is_move:
        for key in knight_coors.keys():
            if key not in next_knight_coors:
                next_knight_coors[key] = knight_coors[key]

        knight_coors = next_knight_coors
        fight(i)
        state = update_state()
    #     print(knight_coors)
    #
    # for a in state:
    #     print(a)
    # print('-----------')

for val in damaged.values():
    total += val
print(total)