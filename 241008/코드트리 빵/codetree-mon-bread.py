from collections import deque


def is_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


def find_min_distance(x, y):
    q = deque()
    q.append((x, y))
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 2로 표시 될 시 해당 부분으로 움직이지 못한다.
            if is_range(nx, ny) and not visited[nx][ny] and board[nx][ny] < 2:
                visited[nx][ny] = True
                if board[nx][ny] == 1:
                    return [nx, ny]
                else:
                    q.append((nx, ny))


# 1과 2 과정
def move_person(sx, sy, num):
    global arrived

    tx, ty = people_target_coors[num]
    min_dist = 987654321
    min_d = 0
    for d in range(4):
        # 방향에 따라 최단거리 측정하기
        visited = [[False] * N for _ in range(N)]
        q = deque()
        x = sx + dx[d]
        y = sy + dy[d]
        # 범위를 벗어나면 
        if not is_range(x, y):
            continue
        q.append((x, y, 0))
        visited[x][y] = True
        while q:
            x, y, cnt = q.popleft()
            if x == tx and y == ty:
                if min_dist > cnt:
                    min_dist = cnt
                    min_d = d
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if is_range(nx, ny) and visited[nx][ny] == 0 and board[nx][ny] < 2:
                    visited[nx][ny] = True
                    q.append((nx, ny, cnt + 1))
    ax, ay = sx + dx[min_d], sy + dy[min_d]
    if ax == tx and ay == tx:
        arrived += 1
        # people_target_coors[num] = [-1, -1]
    people[num] = [sx + dx[min_d], sy + dy[min_d]]


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
people_target_coors = {}
for i in range(M):
    x, y = map(int, input().split())
    people_target_coors[i] = [x - 1, y - 1]
arrive_time = 0
arrived = 0
people = {}

# 상좌우하
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

while True:
    no_move_coors = []
    if arrive_time < M:
        for i in range(arrive_time + 1):
            if i not in people:
                # 문제에서의 3번 수행
                sx, sy = people_target_coors[i]
                people[i] = [sx, sy]
                x, y = find_min_distance(sx, sy)
                no_move_coors.append((x, y))
            else:
                sx, sy = people[i]
                move_person(sx, sy, i)
                if people[i] == people_target_coors[i]:
                    no_move_coors.append((people[i][0], people[i][1]))
    else:
        # 순서대로 시작
        for i in range(M):
            sx, sy = people[i]
            move_person(sx, sy, i)
            if people[i] == people_target_coors[i]:
                no_move_coors.append((people[i][0], people[i][1]))
    # 1분씩 돌면서 편의점에 도착하거나 베이스 캠프에 가는 등의 좌표들을 통해 못가도록 설정
    for x, y in no_move_coors:
        board[x][y] = 2
    if arrived == M:
        print(arrive_time)
        break
    arrive_time += 1