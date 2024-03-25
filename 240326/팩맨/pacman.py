# 2024-03-25


# 격자 범위 체크
def is_range(x, y):
    if x < 0 or x >= 4 or y < 0 or y >= 4:
        return False
    return True


# 몬스터 이동
def move_monsters():
    temp = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            for d in board[x][y]:
                is_set = False
                for k in range(8):
                    nd = (d + k) % 8
                    nx = x + dx[nd]
                    ny = y + dy[nd]
                    # 격자를 안벗어나고 팩맨이 없고 몬스터 시체가 없는 경우 이동 가능
                    if is_range(nx, ny) and (nx != r or ny != c) and dead_board[nx][ny] == 0:
                        temp[nx][ny].append(nd)
                        is_set = True
                        break
                if not is_set:
                    temp[x][y].append(d)
    return temp


def move_pack():
    global r, c

    max_cnt = -1 # 0으로 초기화 시 작은 것을 찾을 수 없기에 -1로 초기화
    max_dirs = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                x, y = r, c
                cnt = 0
                visited = []
                for z in [i, j, k]:
                    nx = x + pdx[z]
                    ny = y + pdy[z]
                    if is_range(nx, ny):
                        # 갔던 곳에 다시 갈 수 있는 방향이 있을 수 있다
                        if (nx, ny) not in visited:
                            cnt += len(board[nx][ny])
                        visited.append((nx, ny))
                        x, y = nx, ny
                    else:
                        cnt = -2 # 범위 벗어난 경우를 -2로 초기화
                        break
                if cnt > max_cnt:
                    max_dirs = visited
                    max_cnt = cnt

    r, c = max_dirs[-1]

    # 격자판에서 시체로 만들었으니 빈 값으로 초기화
    for nr, nc in max_dirs:
        if board[nr][nc]:
            board[nr][nc] = []
            dead_board[nr][nc] = 3 # 현재 진행중인 턴이기 때문에 팩맨 움직인 이후 시체 소멸 과정을 지나야돼서 3으로 초기화


# 몬스터 시체 소멸
def remove_dead():
    for i in range(4):
        for j in range(4):
            if dead_board[i][j] > 0:
                dead_board[i][j] -= 1


# 몬스터 복제
def born_monsters():
    for i in range(4):
        for j in range(4):
            board[i][j].extend(born_board[i][j])


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
pdx = [-1, 0, 1, 0]
pdy = [0, -1, 0, 1]

M, T = map(int, input().split())
r, c = map(int, input().split())
r -= 1
c -= 1

board = [[[] for _ in range(4)] for _ in range(4)] # 현재 상태 board
dead_board = [[0] * 4 for _ in range(4)] # 소멸된 몬스터들 정보 board
born_board = [[[] for _ in range(4)] for _ in range(4)] # 새로 부화할 정보 board
result = 0
for _ in range(M):
    x, y, d = map(int, input().split())
    board[x - 1][y - 1].append(d - 1)

for _ in range(T):
    # 1. 몬스터의 복제 진행
    born_board = [[item[:] for item in monsters] for monsters in board]
    # 2. 몬스터 이동
    board = move_monsters()
    # 3. 팩맨 이동
    move_pack()
    # 4. 시체 소멸
    remove_dead()
    # 5. 몬스터 복제
    born_monsters()

for i in range(4):
    for j in range(4):
        result += len(board[i][j])
print(result)