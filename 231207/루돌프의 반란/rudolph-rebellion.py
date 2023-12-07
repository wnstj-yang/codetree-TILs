# 2023-12-07
# 20:35 ~ 24:00
# 루돌프 충돌까지 구현 + 내일 추가 작성

def move():
    pass


# 1. 가장 가까운 산타 향해 돌진
# 2. r, c가 가장 큰 산타
# 3. 8방향 중 산타의 위치와 가장 가까워지는 것
def move_rudolph():
    global r, c

    min_dist = INF
    candidates = {}
    for num, coor in santaPos.items():
        x, y = coor
        dist = (x - r) ** 2 + (y - c) ** 2
        min_dist = min(min_dist, dist)
        if dist not in candidates:
            candidates[dist] = [coor]
        else:
            candidates[dist].append(coor)
    min_list = sorted(candidates.items())[0][1] # 딕셔너리 key값을 기준으로 오름 차순 정렬 이후 좌표값들이 있는 것을 할당
    min_list.sort(key=lambda x:(-x[0], -x[1])) # 가장 가까운 산타들에 대해 r, c좌표가 큰 산타를 구한다
    tx, ty = min_list[0] # 가장 가까운 산타의 좌표
    min_dist = INF
    d = 0
    for i in range(8):
        nx = r + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        dist = (nx - tx) ** 2 + (ny - ty) ** 2
        if dist < min_dist:
            d = i
            min_dist = dist
    r, c = r + dx[d], c + dy[d] # 루돌프의 이동

    # 충돌하는 상황
    if state[r][c] != 0:
        number = state[tx][ty]  # 산타 위치의 번호
        x, y = r, c
        # 충돌이 발생했으므로 격자판을 벗어나는지 확인한다.
        nx, ny = x + dx[d] * C, y + dy[d] * C
        score[number] += C
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            del santaPos[number] # 산타 위치를 없앤다
            state[x][y] = 0 # 격자판에서 나감
        # 격자판을 벗어나지 않는다면
        else:
            stun[number] = 2 # 스턴 먹음
            state[x][y] = 0
            x, y = nx, ny
            # 산타가 방향에 따라 이동한다.
            while True:
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    del santaPos[number]
                    state[x][y] = 0
                    break
                # 비어있다면 넣어주고 끝
                if state[nx][ny] == 0:
                    state[nx][ny] = number
                    break

                else:
                    state[nx][ny] = number
                    number = state[nx][ny]
                    state[x][y] = 0
                    x, y = nx, ny



# 1. 1번부터 P번까지 순서대로 움직임
# 2. 기절했거나 탈락하면 움직임 X
# 3. 루돌프와 가장 가까운 방향으로 이동
def move_santa():
    pass


INF = 987654321
total = 0
# 상우하좌 + 대각선(왼쪽 위 부터 시계방향)
dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, 1, -1]
N, M, P, C, D = map(int, input().split())
r, c = map(int, input().split()) # 루돌프의 좌표, 인덱스에 따라 각 -1
r -= 1
c -= 1
santaPos = {}
state = [[0] * N for _ in range(N)]
score = [0] * (P + 1) # 각 산타 번호에 따라 점수 상태
stun = [0] * (P + 1) # 산타 번호들에 맞는 기절 상태
for _ in range(P):
    p, x, y = map(int, input().split())
    santaPos[p] = [x - 1, y - 1]
    state[x - 1][y - 1] = p

for _ in range(M):
    move_rudolph()
    break