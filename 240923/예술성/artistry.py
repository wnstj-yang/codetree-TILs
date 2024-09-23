# 1. 점수 계산
# 2. 회전

from collections import deque


def get_groups(x, y):
    q = deque()
    q.append((x, y))
    coors = [(x, y)]
    visited[x][y] = True
    target = board[x][y]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]:
                continue
            if board[nx][ny] == target:
                q.append((nx, ny))
                visited[nx][ny] = True
                coors.append((nx, ny))
    return coors
            

def calculate(group_1, group_2):
    criteria = board[group_1[0][0]][group_1[0][1]]
    target = board[group_2[0][0]][group_2[0][1]]
    border_cnt = 0
    for x, y in group_1:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue 
            if board[nx][ny] == target and (nx, ny) in group_2:
                border_cnt += 1
    # print((len(group_1) + len(group_2)) * criteria * target * border_cnt)
    return (len(group_1) + len(group_2)) * criteria * target * border_cnt
    
def rotate():
    new_board = [[0] * N for _ in range(N)]
    mid = N // 2
    # 십자 모양을 돌린다.
    for idx in range(N):
        new_board[mid][idx] = board[idx][mid]
        new_board[N - 1 - idx][mid] = board[mid][idx]
    
    # 순서대로 4개의 정사각형에 90도 회전을 진행해준다
    # 1. 왼쪽 상단
    for i in range(mid):
        for j in range(mid):
            new_board[j][mid - i - 1] = board[i][j]
    # 2. 오른쪽 상단
    for i in range(mid):
        for j in range(mid + 1, N):
            new_board[j - mid - 1][N - i - 1] = board[i][j]
    # 3. 왼쪽 하단
    idx = 0
    for i in range(mid + 1, N):
        for j in range(mid):
            new_board[mid + 1 + j][mid - 1 - idx] = board[i][j]
        idx += 1
    # 4. 오른쪽 하단
    idx = 0
    for i in range(mid + 1, N):
        for j in range(mid + 1, N):
            new_board[j][N - 1 - idx] = board[i][j]
        idx += 1
    return new_board

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
total = 0 # 조화로움 총합

# 3회전까지 진행
for _ in range(4):
    visited = [[False] * N for _ in range(N)]
    groups = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                groups.append(get_groups(i, j))
    for i in range(len(groups) - 1):
        for j in range(i + 1, len(groups)):
            total += calculate(groups[i], groups[j])
    # print(total)
    # for z in board:
    #     print(z)
    # print('after')
    board = rotate()
    # for i in board:
    #     print(i)
print(total)