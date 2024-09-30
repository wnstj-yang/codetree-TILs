def is_range(x, y):
    if x < 0 or x >= 4 or y < 0 or y >= 4:
        return False
    return True


def replicate():
    for x in range(4):
        for y in range(4):
            for d in board[x][y]:
                monster_egg[x][y].append(d)


# 격자를 벗어나면 반시계 방향으로 45도 회전 - 가능할때까지 움직임 가능하면 움직임
def move_monsters():
    new_board = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            for d in board[x][y]:
                is_done = False
                nd = d
                for k in range(8):
                    nd = (d + k) % 8
                    nx = x + dx[nd]
                    ny = y + dy[nd]
                    if not is_range(nx, ny) or (nx == px and ny == py) or dead_count[nx][ny] > 0:
                        # d = (d + 1) % 8
                        continue
                    new_board[nx][ny].append(nd)
                    is_done = True
                    break
                if not is_done:
                    new_board[nx][ny].append(d)
    return new_board

def move_pacman():
    global px, py

    max_cnt = 0
    max_coors = []
    for d1 in range(4):
        for d2 in range(4):
            for d3 in range(4):
                x, y = px, py
                cnt = 0
                visited = []
                for d in [d1, d2, d3]:
                    nx = x + p_dx[d]
                    ny = y + p_dy[d]
                    if is_range(nx, ny) and (nx, ny) not in visited:
                        cnt += len(board[nx][ny])
                        x, y = nx, ny
                        visited.append((nx, ny))
                    else:
                        cnt = -1
                        break

                if cnt > max_cnt:
                    max_cnt = cnt
                    max_coors = [d1, d2, d3]
    # print(max_coors, px, py)
    for d in max_coors:
        px = px + p_dx[d]
        py = py + p_dy[d]
        board[px][py] = []
        dead_count[px][py] = 3 # 현재 돌고 있는 턴에 소멸을 하므로 2턴 유지를 위해 3으로 설정
                

def born_monster():
    for x in range(4):
        for y in range(4):
            for d in monster_egg[x][y]:
                board[x][y].append(d)


def decrease_dead_count():
    for x in range(4):
        for y in range(4):
            if dead_count[x][y] > 0:
                dead_count[x][y] -= 1


# 위쪽 방향으로 시작해서 반시계로 대각선 포함 진행
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
# 팩맨 우선순위대로 상좌하우
p_dx = [-1, 0, 1, 0]
p_dy = [0, -1, 0, 1]
total_lived = 0
board = [[[] for _ in range(4)] for _ in range(4)]
dead_count = [[0] * 4 for _ in range(4)] # 시체 있는 시간
M, T = map(int, input().split())
px, py = map(int, input().split())
px -= 1
py -= 1
for _ in range(M):
    x, y, d = map(int, input().split())
    board[x - 1][y - 1].append(d - 1)

for _ in range(T):
    monster_egg = [[[] for _ in range(4)] for _ in range(4)]
    replicate()
    # for i in board:
    #     print(i)
    # print('------------')
    board = move_monsters()
    # for i in board:
    #     print(i)
    # print()
    move_pacman()
    # for i in board:
    #     print(i)
    # print('----------팩맨먹음--')
    # for i in monster_egg:
    #     print(i)
    # print('-------복제--------')
    born_monster()
    decrease_dead_count()

# for i in board:
#     print(i)
# print('----------마지막결과--')

for x in range(4):
    for y in range(4):
        total_lived += len(board[x][y])
print(total_lived)