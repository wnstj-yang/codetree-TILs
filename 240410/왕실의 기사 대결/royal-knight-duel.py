# 2024-04-10


def is_range(x, y):
    if x < 0 or x >= L or y < 0 or y >= L:
        return False
    return True


# 기사 움직이기
def check_knight(check_list, d):
    candidates = set()
    for k in check_list:
        for x, y in knights[k][1]:
            nx = x + dx[d]
            ny = y + dy[d]
            if is_range(nx, ny):
                if board[nx][ny] == 2:
                    return [-1]
                # move_list에서 이미 후보인 k가 같은 영역이므로 포함시키지 않는다.
                if knight_board[nx][ny] not in check_list and knight_board[nx][ny] != 0:
                    candidates.add(knight_board[nx][ny])
            else:
                return [-1]
    # 빈 리스트이면 옮겨져도 빈 칸이라 가능함. 즉, 끝
    return list(candidates)


def move_knights(move_list, d):
    for k in move_list:
        next_list = []
        for x, y in knights[k][1]:
            nx = x + dx[d]
            ny = y + dy[d]
            next_list.append((nx, ny))
        knights[k][1] = next_list
    next_board = [[0] * L for _ in range(L)]
    for k, coors in knights.items():
        for x, y in coors[1]:
            next_board[x][y] = k
    return next_board


def damage_knights(damage_list, knight):
    for k in damage_list:
        cnt = 0
        if k == knight:
            continue
        for x, y in knights[k][1]:
            if board[x][y] == 1:
                cnt += 1
        if knights[k][0] - cnt <= 0:
            for x, y in knights[k][1]:
                knight_board[x][y] = 0
            del knights[k]
            del damaged[k]
        else:
            knights[k][0] -= cnt
            damaged[k] += cnt



L, N, Q = map(int, input().split())
# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
total = 0 # 생존한 기사들의 총 받은 데미지 합
board = [list(map(int, input().split())) for _ in range(L)]
knight_board = [[0] * L for _ in range(L)] # 기사들의 크기 격자판
knights = {}
damaged = {}
for i in range(1, N + 1):
    r, c, h, w, k = map(int, input().split())
    r -= 1
    c -= 1
    knights[i] = [k, []]
    damaged[i] = 0
    for x in range(r, r + h):
        for y in range(c, c + w):
            knight_board[x][y] = i
            knights[i][1].append((x, y))
for i in range(1, Q + 1):
    num, d = map(int, input().split())
    move_check = [num]
    # print('before knights', knights)
    while True:
        result = check_knight(move_check, d)
        if result:
            if result[0] == -1:
                move_check = []
                break
            else:
                move_check.extend(result)
        else:
            break

    knight_board = move_knights(move_check, d)
    damage_knights(move_check, i)
    # print('after knights', knights)

# print(knights)
# print(damaged)
# for i in knight_board:
#     print(i)
print(sum(damaged.values()))