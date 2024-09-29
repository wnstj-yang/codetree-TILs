from collections import deque

# 범위 체크하기
def is_out_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return True
    return False


# 나무 성장
def grow_trees():
    for x in range(N):
        for y in range(N):
            if board[x][y] > 0:
                cnt = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if not is_out_range(nx, ny) and board[nx][ny] > 0:
                        cnt += 1
                board[x][y] += cnt
                        

# 나무 번식
def spread_trees():
    add_tree_board = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if board[x][y] > 0 and toxic_board[x][y] == 0:
                directions = []
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    # 조건이 많아 우선 범위를 벗어나거나 벽인 경우 넘어간다
                    if is_out_range(nx, ny) or board[nx][ny] == -1:
                        continue
                    # 제초제가 없고 나무도 없는 곳에 번식할 좌표를 넣는다
                    if board[nx][ny] == 0 and toxic_board[nx][ny] == 0:
                        directions.append(k)
                if len(directions) > 0:
                    add_tree = board[x][y] // len(directions)
                    for d in directions:
                        add_tree_board[x + dx[d]][y + dy[d]] += add_tree
    # 번식이 된 상태를 기존 나무들의 board에 더해준다
    for x in range(N):
        for y in range(N):
            board[x][y] += add_tree_board[x][y]


# 제초제 뿌리기
def spread_toxic():
    global total

    most_toxic = 0
    mx, my = 0, 0
    toxic_coors = []
    for x in range(N):
        for y in range(N):
            if board[x][y] > 0 and toxic_board[x][y] == 0:
                cnt = board[x][y]
                coors = [(x, y)]
                for d in range(4):
                    for k in range(1, K + 1):    
                        nx = x + cx[d] * k
                        ny = y + cy[d] * k
                        if is_out_range(nx, ny):
                            break
                        if board[nx][ny] == -1:
                            break
                        if board[nx][ny] >= 0 and toxic_board[nx][ny] == 0:
                            cnt += board[nx][ny]
                            coors.append((nx, ny))
                            if board[nx][ny] == 0:
                                break

                if cnt > most_toxic:
                    most_toxic = cnt
                    mx, my = x, y
                    toxic_coors = coors
    for x, y in toxic_coors:
        total += board[x][y]
        board[x][y] = 0
        toxic_board[x][y] = C + 1 # 감소 수를 남아있는 년수에서 + 1을 통해 계산
    # print('제초제 뿌린 이후 ')
    # for z in board:
    #     print(z)
    # print()
    

def decrease_toxic():
    for x in range(N):
        for y in range(N):
            if toxic_board[x][y] > 0:
                toxic_board[x][y] -= 1
    # print('회차 이후 감소')
    # for i in toxic_board:
    #     print(i)
    # print('tocix')


N, M, K, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
toxic_board = [[0] * N for _ in range(N)] # 제초제 남아있는 년 수
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 왼쪽 대각선부터 시계방향
cx = [-1, -1, 1, 1]
cy = [-1, 1, 1, -1]
total = 0 # 총 박멸한 나무 그루 수

for _ in range(M):
    decrease_toxic()
    grow_trees()
    # for i in board:
    #     print(i)
    # print()
    spread_trees()
    # for i in board:
    #     print(i)
    # print()
    spread_toxic()
print(total)