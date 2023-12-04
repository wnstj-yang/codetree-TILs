# 2023-12-04
# 21:30 ~ 21:43


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
        # 기사들의 좌표값 중 움직인 것을 파악하고 명령을 받은 기사를 제외한다.
        if key == num or key not in moved:
            continue
        # 기사들이 움직인 이후 함정이 있는 개수를 카운트
        for x, y in values:
            if board[x][y] == 1:
                cnt += 1
        # 각 생명과 피해입은 것을 체크
        life[key] -= cnt
        damaged[key] += cnt
        # 0보다 작으면 체스판에서 사라진다.
        if life[key] <= 0:
            del life[key]
            del damaged[key]
            delete_keys.append(key) # 순회 중 삭제는 불가하여 삭제할 기사의 번호를 체크
    # 삭제할 기사 삭제
    for k in delete_keys:
        del knight_coors[k]


# 좌표값들을 바탕으로 명령 이후 기사의 상태를 갱신한다.
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
life = {} # 생명
damaged = {} # 대미지 받은 수
knight_coors = {} # 각 기사가 존재하는 직사각형 크기에 대한 좌표 값
total = 0
for i in range(1, N + 1):
    r, c, h, w, k = map(int, input().split())
    life[i] = k
    damaged[i] = 0
    r -= 1
    c -= 1
    knight_coors[i] = [] # 각 기사의 좌표
    # 기사의 직사각형 크기만큼 번호로 초기화
    for x in range(r, r + h):
        for y in range(c, c + w):
            state[x][y] = i
            knight_coors[i].append((x, y))

for z in range(Q):
    i, d = map(int, input().split())
    # 기사가 없어졌는데도 부를 수 있기에 없다면 이후 로직 수행 X
    if i not in life:
        continue
    knights = [i]
    next_knight_coors = {} # 움직인 이후의 각 기사의 좌표
    moved = [] # 움직인 기사 판별
    is_move = True # 기사들을 밀어내면서 전부 밀어낼 수 있는지 판단
    # 기사들을 밀어내면서 움직인다.
    while True:
        knights = move_knights(knights, d)
        moved.extend(knights)
        # 개수가 없다면 밀어냄이 끝났다고 판단
        if len(knights) == 0:
            break
        # 첫 번째 값이 -1이면 격자판을 벗어나거나 벽을 만난 것이므로 밀어낼 수 없다.
        elif knights[0] == -1:
            is_move = False
            break
    # 밀어낼 수 있으면 움직인 기사의 좌표를 갱신
    # 밀어낼 수 없으면 그대로
    if is_move:
        # 밀어냄의 영향을 받지 않은 기사의 직사각형도 존재하기에 체크해준다
        for key in knight_coors.keys():
            if key not in next_knight_coors:
                next_knight_coors[key] = knight_coors[key]

        knight_coors = next_knight_coors
        fight(i) # 대미지
        state = update_state() # 현재 기사들 상태 갱신

for val in damaged.values():
    total += val
print(total)