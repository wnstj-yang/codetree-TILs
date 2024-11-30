from collections import deque

def calculate_dist(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def is_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True

def interact(x, y, d):
    pass

# 루돌프 움직임
def move_deer():
    global r, c

    santa_list = []
    # 1. 돌진할 산타 선택
    for i in range(N):
        for j in range(N):
            # 살아있는 산타이고 루돌프가 아니며
            if board[i][j] != 0 and santa_state[board[i][j]] == 0 and not (i == r and j == c):
                dist = calculate_dist(i, j, r, c)
                santa_list.append([dist, i, j, board[i][j]])
    # 2. 인접한 8방향 중 돌진할 산타와 가장 가까워 지는 방향으로 한 칸 돌진
    if santa_list:
        santa_list.sort(key=lambda x:(x[0], -x[1], -x[2]))
        x, y, santa = santa_list[0][1], santa_list[0][2], santa_list[0][3]
        min_val, d = 987654321, 0
        for i in range(8):
            nx = r + dx[i]
            ny = c + dy[i]
            if is_range(nx, ny):
                dist = calculate_dist(nx, ny, x, y)
                if dist < min_val:
                    min_val = dist
                    d = i
        # 3. 구해진 방향으로 루돌프를 이동시킨다.
        r = r + dx[d]
        c = c + dy[d]
        # 4. 움직였더니 산타가 있으면 충돌 발생
        if board[r][c]:
            santa_score[santa] += c
            # TODO: 여기서 부터 상호작용 발생 


# 산타 움직임
def move_santa():
    for i in range(1, P + 1):
        pass


def remove_santa_state():
    pass

# 루돌프 - 우선순위 높은 산타. 가장 가까워지는 방향으로 돌진

# 상우하좌 + 대각선
dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, 1, -1]
N, M, P, C, D = map(int, input().split())
r, c = map(int, input().split())
r -= 1
c -= 1
santa_loc = {}
santa_state = {}
santa_score = {}
board = [[0] * N for _ in range(N)]
for i in range(1, P + 1):
    num, x, y = map(int, input().split())
    x -= 1
    y -= 1
    santa_state[num] = True
    board[x][y] = num
    santa_loc[num] = [x, y]
    santa_score[num] = 0
