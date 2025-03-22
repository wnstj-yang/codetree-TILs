def is_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True

def move(x, y):
    global length, length_cnt, times, d, total_dust
    tx = x + dx[d]
    ty = y + dy[d]

    curr = board[tx][ty]
    board[tx][ty] = 0
    curr_dust = 0 # 비율에 맞는 먼지 수

    for nxd, nyd, ratio in directions[d]:
        nx = tx + nxd
        ny = ty + nyd
        dust = int(curr * ratio)
        curr_dust += dust
        if is_range(nx, ny):
            board[nx][ny] = int(board[nx][ny] + dust)
        else:
            total_dust += dust
    nx = tx + dx[d]
    ny = ty + dy[d]
    if is_range(nx, ny):
        board[nx][ny] += (curr - curr_dust)
    else:
        total_dust += (curr - curr_dust)

    length_cnt += 1
    if length_cnt == length:
        times += 1
        length_cnt = 0
        d = (d + 1) % 4
    if times == 2:
        if length != N - 1:
            times = 0
            length += 1
    return tx, ty
total_dust = 0

# 좌하우상
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
length = 1 # 길이
length_cnt = 0 # 길이만큼 몇번 갔는지
times = 0 # length 길이 방향으로 몇칸 갔는지
d = 0
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
x, y = N // 2, N // 2
directions = {
    0: [
        (-2, 0, 0.02), (-1, -1, 0.1), (-1, 0, 0.07), (-1, 1, 0.01),
        (0, -2, 0.05), (1, -1, 0.1), (1, 0, 0.07), (1, 1, 0.01), (2, 0, 0.02)
    ],
    1: [
        (-1, -1, 0.01), (-1, 1, 0.01), (0, -2, 0.02), (0, -1, 0.07),
        (0, 1, 0.07), (0, 2, 0.02), (1, -1, 0.1), (1, 1, 0.1), (2, 0, 0.05)
    ],
    2: [
        (-2, 0, 0.02), (-1, -1, 0.01), (-1, 0, 0.07), (-1, 1, 0.1),
        (0, 2, 0.05), (1, -1, 0.01), (1, 0, 0.07), (1, 1, 0.1), (2, 0, 0.02)
    ],
    3: [
        (-2, 0, 0.05), (-1, -1, 0.1), (-1, 1, 0.1), (0, -2, 0.02),
        (0, -1, 0.07), (0, 1, 0.07), (0, 2, 0.02), (1, -1, 0.01), (1, 1, 0.01)
    ],
}
while True:
    if x == 0 and y == 0:
        break
    x, y = move(x, y)
print(total_dust)
