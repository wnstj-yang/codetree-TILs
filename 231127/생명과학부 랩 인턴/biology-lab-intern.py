# 2023-11-27
# 13:30 ~ 14:05 / 17: 35 ~ 19:00


# 순서대로 열을 움직이면서 곰팡이를 채취
def get_mold(j):
    global total

    for i in range(N):
        if board[i][j]:
            total += board[i][j][0]
            board[i][j] = []
            return


# 격자판 벗어날 떄 방향 전환
def check_direction(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    else:
        return 2


# 곰팡이들의 이동
def move_mold():
    next_board = [[[] for _ in range(M)] for _ in range(N)]
    for x in range(N):
        for y in range(M):
            if board[x][y]:
                b, s, d = board[x][y]
                ns = s # 속도를 줄여나가면서 이동을 한다고 가정하기 떄문에 새로운 변수에 속도 저장
                ox, oy = x, y # x, y로 for문을 돌아서 따로 변수로 설정
                while ns:
                    nx = ox + dx[d]
                    ny = oy + dy[d]
                    
                    # 격자판 범위를 벗어낫으므로 방향 전환
                    if nx < 0 or nx >= N or ny < 0 or ny >= M:
                        d = check_direction(d)
                        nx = ox + dx[d]
                        ny = oy + dy[d]
                    ns -= 1
                    ox, oy = nx, ny # 이동한 좌표 값들을 갱신
                # 마지막 이동한 만큼 이동하고 다음 격자판에 넣는다
                next_board[ox][oy].append([b, s, d])
                
    # 이동이 완료된 부분에서 여러 개의 곰팡이가 존재할 경우 
    for i in range(N):
        for j in range(M):
            if next_board[i][j]:
                next_board[i][j].sort(key=lambda x:(-x[0]))
                # 가장 큰 곰팡이가 살아남으므로 크기로 내림차순 정렬한 첫 번쨰 값을 넣어준다
                next_value = [next_board[i][j][0][0], next_board[i][j][0][1], next_board[i][j][0][2]]
                next_board[i][j] = next_value
    return next_board


N, M, K = map(int, input().split())

board = [[[] for _ in range(M)] for _ in range(N)]
total = 0
# 문제 조건대로 1 ~ 4 / 상하우좌 순
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(K):
    x, y, s, d, b = map(int, input().split())
    # x, y, d 같은 경우 인덱스 상을 위해 1을 줄인다.
    board[x - 1][y - 1] = [b, s, d - 1] # [크기, 움직이는 거리, 방향]


# 열을 왼쪽에서 오른쪽으로 범위까지 모든 열 검사 진행
for search in range(M):
    get_mold(search)
    board = move_mold()

print(total)