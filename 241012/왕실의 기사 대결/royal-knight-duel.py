from collections import deque

# 기사 이동 시 벽 체크
def move_check(num, d):
    knight_list = [num]
    visited = [num]
    can_move = True
    # print(num, d)
    while knight_list:
        knight_num = knight_list.pop()
        r, c, h, w = knights[knight_num]
        for x in range(r, r + h):
            for y in range(c, c + w):
                # 현재 기사의 방향으로 한 칸씩 판단한다
                nx = x + dx[d]
                ny = y + dy[d]
                # 벽을 만나거나 범위를 벗어나면 움직이지 못한다.
                if nx < 0 or nx >= L or ny < 0 or ny >= L or board[nx][ny] == 2:
                    return [-1]
                # 이동하는 경로에 현재 기사 이동에 겹치는 부분 없이, 기사 번호 체크
                if knight_board[nx][ny] > 0 and knight_board[nx][ny] not in visited:
                    visited.append(knight_board[nx][ny])
                    knight_list.append(knight_board[nx][ny])
    # print(visited)
    return visited

# 필요한 기사들 이동
def move_knights(move_list, start_num, d):
    next_knight_board = [[0] * L for _ in range(L)]
    for num in move_list:
        r, c, h, w = knights[num]
        damage = 0
        for x in range(r, r + h):
            for y in range(c, c + w):
                nx = x + dx[d]
                ny = y + dy[d]
                next_knight_board[nx][ny] = num
                if board[nx][ny] == 1:
                    damage += 1
        # 첫 기사 위치 갱신
        knights[num][0], knights[num][1] = r + dx[d], c + dy[d]
        if num != start_num:
            damaged[num][1] -= damage
            # print(num, damaged)
            # 대미지를 다 입었을 때
            if damaged[num][1] <= 0:
                damaged[num][1] = 0
                r, c = knights[num][0], knights[num][1]
                for x in range(r, r + h):
                    for y in range(c, c + w):
                        next_knight_board[x][y] = 0
    for num, values in damaged.items():
        if num not in move_list and values[1] > 0:
            r, c, h, w = knights[num]
            for x in range(r, r + h):
                for y in range(c, c + w):
                    next_knight_board[x][y] = num

    return next_knight_board


L, N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(L)]
total_damage = 0
knights = {}
knight_board = [[0] * L for _ in range(L)]
damaged = {}
# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(1, N + 1):
    r, c, h, w, k = map(int, input().split())
    r -= 1
    c -= 1
    for x in range(r, r + h):
        for y in range(c, c + w):
            knight_board[x][y] = i
    knights[i] = [r, c, h, w]
    damaged[i] = [k, k]

for i in range(Q):
    num, d = map(int, input().split())
    if damaged[num][1] == 0:
        continue
    move_list = move_check(num, d)
    if move_list[0] != -1:
        knight_board = move_knights(move_list, num, d)
    # for z in knight_board:
    #     print(z)
    # print(knights)
    # print('----')
total = 0
for life, hurt in damaged.values():
    if hurt > 0:
        total += (life - hurt)    
print(total)