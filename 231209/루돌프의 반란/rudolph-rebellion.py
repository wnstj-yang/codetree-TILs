# 2023-12-07
# 20:35 ~ 24:00
# 지이이이인짜 돌아버리겠네

# 1. 가장 가까운 산타 향해 돌진
# 2. r, c가 가장 큰 산타
# 3. 8방향 중 산타의 위치와 가장 가까워지는 것
def move_rudolph():
    global r, c, santaPos

    min_dist = INF
    candidates = {}

    for i in range(1, len(santaPos)):
        x, y = santaPos[i]
        if x == -1 and y == -1:
            continue
        dist = (x - r) ** 2 + (y - c) ** 2
        min_dist = min(min_dist, dist)
        if dist not in candidates:
            candidates[dist] = [(x, y)]
        else:
            candidates[dist].append((x, y))
    min_list = sorted(candidates.items())[0][1] # 딕셔너리 key값을 기준으로 오름 차순 정렬 이후 좌표값들이 있는 것을 할당
    min_list.sort(key=lambda x:(-x[0], -x[1])) # 가장 가까운 산타들에 대해 r, c좌표가 큰 산타를 구한다
    tx, ty = min_list[0] # 가장 가까운 산타의 좌표
    min_dist = INF
    d = 0
    for i in range(8):
        nx = r + dx[i]
        ny = c + dy[i]
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
        state[r][c] = 0
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            state[x][y] = 0 # 격자판에서 나감
        # 격자판을 벗어나지 않는다면
        else:
            stun[number] = 2  # 스턴 먹음
            if state[nx][ny] == 0:
                # state[x][y] = 0
                state[nx][ny] = number
            else:
                next_number = state[nx][ny]
                state[nx][ny] = number
                number = next_number
                state[x][y] = 0
                x, y = nx, ny
                # 산타가 방향에 따라 이동한다.
                while True:
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        break
                    # 비어있다면 넣어주고 끝
                    if state[nx][ny] == 0:
                        state[nx][ny] = number
                        break
                    # 다음 움직이는 곳에도 산타가 존재하면 밀어낸다 - 상호작용
                    else:
                        next_number = state[nx][ny]
                        state[nx][ny] = number
                        number = next_number
                        # state[x][y] = 0
                        x, y = nx, ny # 좌표 갱신

    santaPos = [(-1, -1)] * (P + 1)
    for i in range(N):
        for j in range(N):
            if state[i][j] != 0:
                santaPos[state[i][j]] = (i, j)


def move_santa():
    global santaPos

    for num in range(1, len(santaPos)):
        x, y = santaPos[num]
        # 탈락하거나 기절하면 X
        if (x == -1 and y == -1) or stun[num] > 0:
            continue
        min_dist = INF
        d = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 격자판을 벗어나거나 산타가 존재하면 X
            if nx < 0 or nx >= N or ny < 0 or ny >= N or state[nx][ny] != 0:
                continue
            dist = (nx - r) ** 2 + (ny - c) ** 2

            if dist < min_dist:
                d = k
                min_dist = dist

        if min_dist != INF and min_dist < (x - r) ** 2 + (y - c) ** 2:
            sx = x + dx[d]
            sy = y + dy[d]
            # sx, sy가 움직여야 하는 곳

            # 산타가 루돌프한테 박았다.
            if sx == r and sy == c:
                d = (d + 2) % 4  # 반대 방향으로 방향 설정
                number = state[x][y]
                score[number] += D
                # 루돌프에 박고 나서 반대방향으로 D만큼 이동
                nx = sx + dx[d] * D
                ny = sy + dy[d] * D

                # 튕겨나가서 격자 밖으로 나가면 끝
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    state[x][y] = 0 # 기존 있는 곳은 0으로 초기화
                    santaPos[number] = (-1, -1)
                # 튕겨 나간 곳에 비어있거나 본인이 있었던 위치로 돌아오면
                elif state[nx][ny] == 0 or (x == nx and y == ny):
                    number = state[x][y]
                    stun[number] = 2
                    state[x][y] = 0
                    state[nx][ny] = number
                    santaPos[number] = (nx, ny)
                # 튕겨 나간 곳에 산타가 존재하는 경우
                else:
                    number = state[x][y]
                    stun[number] = 2  # 스턴 먹음
                    next_number = state[nx][ny]
                    state[nx][ny] = number
                    santaPos[number] = (nx, ny)
                    number = next_number
                    state[x][y] = 0
                    x, y = nx, ny
                    # 산타가 방향에 따라 이동한다.
                    while True:
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            break
                        # 비어있다면 넣어주고 끝
                        if state[nx][ny] == 0:
                            state[nx][ny] = number
                            santaPos[number] = (nx, ny)
                            break
                        # 다음 움직이는 곳에도 산타가 존재하면 밀어낸다 - 상호작용
                        else:
                            next_number = state[nx][ny]
                            state[nx][ny] = number
                            santaPos[number] = (nx, ny)
                            number = next_number
                            # state[x][y] = 0
                            x, y = nx, ny  # 좌표 갱신

            # 산타 움직임 - 산타가 있는지 없는지 구분할 필요는 없다. 방향 구할 때 이미 없는 위치를 구했기 때문
            else:
                number = state[x][y]
                state[x][y] = 0
                santaPos[number] = (sx, sy)
                state[sx][sy] = number

    santaPos = [(-1, -1)] * (P + 1)
    for i in range(N):
        for j in range(N):
            if state[i][j]:
                santaPos[state[i][j]] = (i, j)


def decrease_stun():
    for i in range(1, len(stun)):
        if stun[i] > 0:
            stun[i] -= 1


INF = 987654321
total = 0
# 상우하좌 + 대각선(왼쪽 위 부터 시계방향)
dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, 1, -1]
N, M, P, C, D = map(int, input().split())
r, c = map(int, input().split()) # 루돌프의 좌표, 인덱스에 따라 각 -1
r -= 1
c -= 1
santaPos = [(-1, -1)] * (P + 1)
state = [[0] * N for _ in range(N)]
score = [0] * (P + 1) # 각 산타 번호에 따라 점수 상태
stun = [0] * (P + 1) # 산타 번호들에 맞는 기절 상태
for _ in range(P):
    p, x, y = map(int, input().split())
    santaPos[p] = (x - 1, y - 1)
    state[x - 1][y - 1] = p

for z in range(M):
    move_rudolph()
    move_santa()
    decrease_stun()
    is_out = True

    for i in range(1, len(santaPos)):
        if santaPos[i] != (-1, -1):
            score[i] += 1
            is_out = False

    if is_out:
        break

print(*score[1:])