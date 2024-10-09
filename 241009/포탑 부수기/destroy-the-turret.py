from collections import deque



# 1. 공격자 선정 - 가장 약한 포탑(공격력이 가장 낮은 포탑)을 찾는다
def find_attacker(time):
    min_val = 987654321
    min_coors = []
    # 1.1. 가장 약한 포탑의 공격력을 구한다
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                min_val = min(min_val, board[i][j])
    
    # 1.2. 약한 포탑의 좌표들과 최근 공격한 시간, 행과 열 합, 열 값을 후보에 넣는다
    for x in range(N):
        for y in range(M):
            if board[x][y] == min_val:
                # 현재 포탑의 공격 상태, 행과 열 합, 열, x, y좌표 순으로 저장
                min_coors.append((attack_state[x][y], x + y, y, x, y))
    min_coors.sort(key=lambda x:(-x[0], -x[1], -x[2]))
    # 선정된 공격자의 좌표 값
    x, y = min_coors[0][-2], min_coors[0][-1]
    board[x][y] += (N + M) # 공격력 증가
    attack_state[x][y] = time # 공격시간 갱신
    related_attack[x][y] = True # 공격에 관련됨
    return [x, y]

# 2. 선정된 공격자의 공격 - 가장 강한 포탑 공격
def attack(ax, ay, time):
    max_val = 0
    max_coors = []
    # 2.1. 가장 강한 포탑의 공격력을 구한다
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                max_val = max(max_val, board[i][j])
    # 2.2. 강한 포탑의 좌표들과 최근 공격한 시간, 행과 열 합, 열 값을 후보에 넣는다
    for x in range(N):
        for y in range(M):
            if board[x][y] == max_val:
                # 현재 포탑의 공격 상태, 행과 열 합, 열, x, y좌표 순으로 저장
                max_coors.append((attack_state[x][y], x + y, y, x, y))
    max_coors.sort(key=lambda x:(x[0], x[1], x[2]))
    x, y = max_coors[0][-2], max_coors[0][-1]
    attack_state[x][y] = time # 공격시간 갱신
    related_attack[x][y] = True # 공격에 관련됨
    attack_done = laser_attack(ax, ay, x, y) # 선정 공격자 좌표 및 공격 당할 좌표
    if not attack_done:
        bomb_attack(x, y, board[ax][ay])

# 2.1. 레이저 공격
def laser_attack(ax, ay, tx, ty):
    q = deque()
    q.append((ax, ay, []))
    visited = [[False] * M for _ in range(N)]
    visited[ax][ay] = True
    while q:
        x, y, coors = q.popleft()
        for i in range(4):
            nx = (x + dx[i]) % N
            ny = (y + dy[i]) % M
            if not visited[nx][ny] and board[nx][ny] > 0:
                if nx == tx and ny == ty:
                    related_attack[tx][ty] = True
                    board[tx][ty] -= board[ax][ay]
                    decrease_val = board[ax][ay] // 2
                    for r, c in coors:
                        related_attack[r][c] = True
                        board[r][c] -= decrease_val
                    return True
                visited[nx][ny] = True
                q.append((nx, ny, coors + [(nx, ny)]))
    return False

# 2.2. 포탄 공격
def bomb_attack(x, y, value):
    # 기존 우하좌상 + 대각선 추가
    ddx = dx + [-1, -1, 1, 1]
    ddy = dy + [-1, 1, 1, -1]
    decrease_val = value // 2
    board[x][y] -= value
    related_attack[x][y] = True
    for i in range(8):
        nx = (x + ddx[i]) % N
        ny = (y + ddy[i]) % M
        if board[nx][ny] > 0:
            related_attack[nx][ny] = True
            board[nx][ny] -= decrease_val

# 3. 포탑 부서짐
def broke_turret():
    for x in range(N):
        for y in range(M):
            if board[x][y] < 0:
                board[x][y] = 0


# 4. 포탑 정비
def repair_turret():
    for x in range(N):
        for y in range(M):
            if not related_attack[x][y] and board[x][y] > 0:
                board[x][y] += 1


# 우하좌상 우선순위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
attack_state = [[0] * M for _ in range(N)]
for i in range(1, K + 1):
    # 부서지지 않은 포탑이 1개면 즉시 중지 !!!!!
    related_attack = [[False] * M for _ in range(N)]
    ax, ay = find_attacker(i)
    attack(ax, ay, i)
    # for z in board:
    #     print(z)
    # print('---')
    broke_turret()
    repair_turret()
    # for z in board:
    #     print(z)
    # print('---')
max_result = 0
for l in board:
    max_result = max(max_result, max(l))
print(max_result)