# 2023-11-21
# 20:50 ~ 21:38


def move_nutrients(d, p):
    # 다음 영양제들의 위치 갱신
    next_nutrients = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if nutrients[i][j]:
                # 영양분이 존재하면 격자 범위를 넘어 서는 부분에서도 나머지연산으로 이어지게끔 처리
                nx = (i + dx[d] * p) % N
                ny = (j + dy[d] * p) % N
                next_nutrients[nx][ny] = True # 영양제 추가
                board[nx][ny] += 1 # 증가
    return next_nutrients


def grow():
    for i in range(N):
        for j in range(N):
            if nutrients[i][j]:
                cnt = 0
                # 8방향 중 2로 나눴을 때 나머지가 1인 값 즉, 홀수이면 대각선을 가리킨다.
                for k in range(8):
                    if k % 2:
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue
                        # 문제 조건에 맞게 1 이상일 때 갯수 증가
                        if board[nx][ny] >= 1:
                            cnt += 1
                board[i][j] += cnt # 대각선에 리브로수가 1 이상을 가진 높이인 갯수를 더해준다


def cut():
    for i in range(N):
        for j in range(N):
            # 영양제를 맞은 땅을 제외하고 높이가 2 이상인 리브로수를 2만큼 잘라낸다
            if not nutrients[i][j] and board[i][j] >= 2:
                nutrients[i][j] = True
                board[i][j] -= 2
            # 격자판을 순서대로 순회하기 때문에 영양제를 맞은 땅의 경우에는 지워준다
            elif nutrients[i][j]:
                nutrients[i][j] = False


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# 조건에 나와있는 방향
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
nutrients = [[False] * N for _ in range(N)]
nutrients[N - 1][0] = True
nutrients[N - 1][1] = True
nutrients[N - 2][0] = True
nutrients[N - 2][1] = True
for _ in range(M):
    d, p = map(int, input().split())
    d -= 1
    nutrients = move_nutrients(d, p)
    grow()
    cut()
total = 0
for i in board:
    total += sum(i)
print(total)