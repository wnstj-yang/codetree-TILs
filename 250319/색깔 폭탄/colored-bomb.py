from collections import deque

def is_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


def search_explosion():
    visited = [[False] * N for _ in range(N)]
    explode_list = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and board[i][j] > 0:
                num = board[i][j]
                visited[i][j] = True
                q = deque()
                q.append((i, j))
                coors = [(i, j)]
                red_coors = []
                cnt, red_cnt = 1, 0
                cx, cy = i, j
                # 총 개수, 빨간색폭탄 개수, 기준점 행, 열
                # 행은 가장 큰, 열은 가장 작은 것
                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if is_range(nx, ny) and not visited[nx][ny] and (board[nx][ny] == 0 or board[nx][ny] == num):
                            visited[nx][ny] = True
                            cnt += 1
                            q.append((nx, ny))
                            coors.append((nx, ny))
                            if board[nx][ny] == 0:
                                red_coors.append((nx, ny))
                                red_cnt += 1
                            # 인접 4방향 상하좌우기 때문에 좌표별로 max, min처리가 가능하다.
                            # 그렇지 대각선이나 그런경우가 있다면 해당 방법은 적용하기 어려울 수 있음. (포함되지 않는 좌표가 택해질 수 있음)
                            else:
                                cx = max(cx, nx)
                                cy = min(cy, ny)

                if cnt > 1:
                    # coors안에는 red도 있기 때문에 정렬로해서 기준점을 구할 수 없다.
                    # coors.sort(key=lambda x:(-x[0], x[1]))
                    # cx, cy = coors[0]
                    explode_list.append([cnt, red_cnt, cx, cy, coors])
                # 빨간부분에 대한 방문표시 초기화
                for rx, ry in red_coors:
                    visited[rx][ry] = False
    if explode_list:
        explode_list.sort(key=lambda x:(-x[0], x[1], -x[2], x[3]))
        return explode_list[0][-1]
    else:
        return []


# 반시계 방향으로 90도 회전
def rotate_90():
    next_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            next_board[N - 1 - j][i] = board[i][j]
    return next_board

# 중력
def gravity():
    for j in range(N):
        cnt = 0
        for i in range(N - 1, -1, -1):
            if board[i][j] == -2:
                cnt += 1
            elif board[i][j] == -1:
                cnt = 0
            else:
                if cnt == 0:
                    continue
                board[i + cnt][j] = board[i][j]
                board[i][j] = -2

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
while True:
    explosion_list = search_explosion()
    if explosion_list:
        # print(explosion_list)
        result += len(explosion_list) ** 2
        for x, y in explosion_list:
            board[x][y] = -2
        gravity()
        board = rotate_90()
        gravity()
    else:
        break

print(result)
