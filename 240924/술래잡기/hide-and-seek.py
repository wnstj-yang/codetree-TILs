# 도망자 움직이기
def move_runners():
    new_board = [[[] for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            distance = abs(x - cx) + abs(y - cy)
            # 도망자가 존재하고 술래와의 거리가 3이하일 때만 움직인다.
            if board[x][y] and distance <= 3:
                for d in board[x][y]:
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        d = (d + 2) % 4
                        nx = x + dx[d]
                        ny = y + dy[d]
                    # 범위를 벗어나서 방향전환 후 한 칸 이동했을 때나 그냥 이동했을 때
                    # 움직이려는 칸에 술래가 있으면 기존 현재 위치에 방향 추가
                    if nx == cx and ny == cy:
                        new_board[x][y].append(d)
                    else:
                        new_board[nx][ny].append(d)
    return new_board


# 술래 움직이기
# 길이가 N - 1이 아닌 이상 해당 길이로 2번씩 움직이고, N - 1이면 3번 움직인다.(방향전환하면서)
def move_catcher():
    global cx, cy, cd, move_cnt, length_cnt, length, isRight

    runner_cnt = 0
    nx = cx + dx[cd]
    ny = cy + dy[cd]
    move_cnt += 1 # 움직인 횟수(length만큼 움직임을 체크한다)
    # 정방향(중앙 -> 첫 위치)
    if isRight:
        # length가 N - 1만큼이면 
        if length == N - 1:
            # length만큼 움직이면 length_cnt 증가 
            if move_cnt == length:
                length_cnt += 1
                move_cnt = 0 # 움직임 초기화
                cd = (cd + 1) % 4 # 방향 전환
                # N - 1이 3번 다된 경우 끝
                if length_cnt == 3:
                    length_cnt = 0
                    if nx == 0 and ny == 0:
                        isRight = False
                        cd = 2
        else:
            if move_cnt == length:
                length_cnt += 1
                move_cnt = 0
                cd = (cd + 1) % 4
                if length_cnt == 2:
                    length += 1
                    length_cnt = 0          
    # 역방향(첫 위치 -> 중앙)
    else:
        # length가 N - 1만큼이면 
        if length == N - 1:
            # length만큼 움직이면 length_cnt 증가 
            if move_cnt == length:
                length_cnt += 1
                move_cnt = 0 # 움직임 초기화
                cd = (cd - 1) % 4 # 방향 전환
                # N - 1이 3번 다된 경우 끝
                if length_cnt == 3:
                    length_cnt = 0
                    length -= 1
        else:
            if move_cnt == length:
                length_cnt += 1
                move_cnt = 0
                cd = (cd - 1) % 4
                if length_cnt == 2:
                    length -= 1
                    length_cnt = 0
                    if nx == N // 2 and ny == N // 2:
                        isRight = True
                        cd = 0
                        length = 1
    cx, cy = nx, ny
    for i in range(3):
        nx = cx + dx[cd] * i
        ny = cy + dy[cd] * i
        
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            break
        if not trees[nx][ny] and len(board[nx][ny]) > 0:
            runner_cnt += len(board[nx][ny])
            board[nx][ny] = []
    return runner_cnt


N, M, H, K = map(int, input().split())

board = [[[] for _ in range(N)] for _ in range(N)] # 도망자 정보 겸 격자판
trees = [[False] * N for _ in range(N)] # 나무 정보
cx, cy = N // 2, N // 2
cd = 0
length = 1
move_cnt = 0
length_cnt = 0
isRight = True # 정방향, 역방향 처리 flag
total = 0
# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for _ in range(M):
    x, y, d = map(int, input().split())
    # 1이면 좌우 - 오른쪽 시작 / 2이면 상하 - 아래 시작
    if d == 1:
        board[x - 1][y - 1].append(1)
    else:
        board[x - 1][y - 1].append(2)
for _ in range(H):
    x, y = map(int, input().split())
    trees[x - 1][y - 1] = True

for k in range(1, K + 1):
    # 1. 도망자 움직임
    board = move_runners()
    check_runners = 0
    # for i in range(N):
    #     for j in range(N):
    #         check_runners += len(board[i][j])
    # if check_runners == 0:
    #     break
    # 2. 술래 움직임
    catched_runners = move_catcher()
    total += (catched_runners * k)
    # for i in board:
    #     print(i)
print(total)