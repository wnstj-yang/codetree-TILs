from collections import deque


def is_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


# 가까운 승객을 찾으러 가는 과정
def search():
    q = deque()
    visited = [[False] * N for _ in range(N)]
    q.append((r, c, C))
    visited[r][c] = True
    passenger_list = []
    # 전기차 위치와 승객이 동일한 경우도 고려
    if len(board[r][c]) > 0:
        for num in board[r][c]:
            if num >= 2:
                return [r, c, C, num]
    while q:
        x, y, dist = q.popleft()
        # print(x, y, dist)
        # 거리
        if dist < 0:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_range(nx, ny) and not visited[nx][ny] and not (len(board[nx][ny]) == 1 and board[nx][ny][0] == 1):
                visited[nx][ny] = True
                if len(board[nx][ny]) > 0:
                    for num in board[nx][ny]:
                        if num >= 2:
                            passenger_list.append((nx, ny, dist - 1, num))
                            break
                q.append((nx, ny, dist - 1))
    if passenger_list:
        passenger_list.sort(key=lambda x:(-x[2], x[0], x[1]))
        x, y, dist, num = passenger_list[0]
        return [x, y, dist, num]
    else:
        return [-1, -1, -1, -1]    


def search_dest(target):
    q = deque()
    q.append((r, c, 0))
    visited = [[False] * N for _ in range(N)]
    visited[r][c] = True
    while q:
        x, y, dist = q.popleft()
        # 거리
        if dist < 0:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_range(nx, ny) and not visited[nx][ny] and not (len(board[nx][ny]) == 1 and board[nx][ny][0] == 1):
                for num in board[nx][ny]:
                    if num == target:
                        return [nx, ny, dist + 1]
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))
    return [-1, -1, -1]


N, M, C = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j]:
            board[i][j].append(row[j])
# 상하좌우
r, c = map(int, input().split())
r -= 1
c -= 1
passenger_state = [1] * (M + 2)
for i in range(M):
    xs, ys, xe, ye = map(int, input().split())
    xs -= 1
    ys -= 1
    xe -= 1
    ye -= 1
    board[xs][ys].append(i + 2) # 출발점
    board[xe][ye].append(-(i + 2)) # 도착점


while True:
    # 1. 가장 가까운 승객 태우러 출동
    x, y, dist, target = search()
    # 모두 -1로 반환된 경우 승객에게 가지 못하고 연료가 없어졌으므로 끝
    if dist == -1:
        answer = -1
        break
    # 받은 정보를 토대로 전기차 좌표, 현재 연료 상태(C) 갱신
    board[x][y].remove(target) # 승객 태움
    r, c, C = x, y, dist

    # 2. 태운 승객의 목적지로 이동한다
    x, y, dist = search_dest(-target)
    if dist == -1:
        answer = -1
        break
    r, c = x, y
    C = C - dist + (dist * 2)
    board[r][c].remove(-target)
    passenger_state[target] = 0

    if sum(passenger_state[2:]) == 0:
        answer = C
        break

print(answer)
