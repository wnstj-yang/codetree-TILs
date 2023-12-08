# 2023-12-07
# 20:35 ~ 24:00
# 루돌프 충돌까지 구현 + 내일 추가 작성

def move():
    pass


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
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            del santaPos[number] # 산타 위치를 없앤다
            state[x][y] = 0 # 격자판에서 나감
        # 격자판을 벗어나지 않는다면
        else:
            stun[number] = 2 # 스턴 먹음
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
                    del santaPos[number]
                    state[x][y] = 0
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
                    state[x][y] = 0
                    x, y = nx, ny # 좌표 갱신
    # TODO : 격자판보고 각 산타들 번호에 따른 좌표 값들 갱신 혹은 필요성 유무 체크하기
    santaPos = [(-1, -1)] * (P + 1)
    for i in range(N):
        for j in range(N):
            if state[i][j]:
                santaPos[state[i][j]] = (i, j)


# 1. 1번부터 P번까지 순서대로 움직임
# 2. 기절했거나 탈락하면 움직임 X
# 3. 루돌프와 가장 가까운 방향으로 이동
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
            # 산타가 루돌프한테 박는다
            if dist < min_dist:
                d = k
                min_dist = dist
        # 최소 거리가 INF이면 움직이지 않기에 움직인 경우 체크
        if min_dist != INF:
            sx = x + dx[d]
            sy = y + dy[d]

            stun[number] = 2 # 스턴 먹음
            next_number = state[nx][ny]
            state[nx][ny] = number
            number = next_number
            state[x][y] = 0
            x, y = nx, ny

            # 산타가 루돌프한테 박았다.
            if sx == r and sy == c:
                d = (d + 2) % 4  # 반대 방향으로 방향 설정
                number = state[x][y]
                score[number] += D
                nx = sx + dx[d] * D
                ny = sy + dy[d] * D
                # 튕겨나가서 격자 밖으로 나가면 끝
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    state[sx][sy] = 0
                # 튕겨 나간 곳에 비어있으면 정착
                elif state[nx][ny] == 0:
                    number = state[x][y]
                    state[x][y] = 0
                    state[sx][sy] = number

            # 산타 움직임
            else:
                number = state[x][y]
                state[x][y] = 0
                state[sx][sy] = number

    santaPos = [(-1, -1)] * (P + 1)
    for i in range(N):
        for j in range(N):
            if state[i][j]:
                santaPos[state[i][j]] = (i, j)

def decrease_stun():
    for i in range(len(stun)):
        stun[i] -= 1
        if stun[i] < 0:
            stun[i] = 0


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
print(santaPos)
for _ in range(M):
    move_rudolph()
    print(santaPos)
    break