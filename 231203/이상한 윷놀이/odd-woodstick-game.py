# 2023-12-03
#


def search(target):
    for i in range(N):
        for j in range(N):
            if state[i][j]:
                # 순회 하면서 말(들)이 존재한다면 인덱스를 알기 위한 enumerate
                for index, info in enumerate(state[i][j]):
                    num, d = info
                    if num == target:
                        return [i, j, d, index]


# 전체 방향 전환 즉, 좌 <-> 우, 상 <-> 하
def change_direction(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    else:
        return 2


def move(x, y, d, idx, target):
    # 흰색 포함 방향으로 움직임을 표시
    nx = x + dx[d]
    ny = y + dy[d]
    is_red = False
    # 격자를 벗어날 때 혹은 파란색인 경우 방향 전환
    if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:
        d = change_direction(d)
        nx = x + dx[d]
        ny = y + dy[d]
        # 전환해도 파란색이거나 격자를 벗어나면 가만히 있는다.
        if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:
            nx, ny = x, y
        # 반면에 빨간색이라면 추후 뒤집는다.
        elif board[nx][ny] == 1:
            is_red = True
    # 아니면 뒤집는다.
    elif board[nx][ny] == 1:
        is_red = True

    # 구했던 인덱스 포함해서 위에 말들이 존재하면 그 끝까지의 리스트 슬라이싱으로 구한다
    group = state[x][y][idx:]
    del state[x][y][idx:] # 기존에 있는 곳은 삭제
    
    # 리스트 슬라이싱한 첫 번째 값은 현재 값이므로 방향이 전환되었다면 갱신
    group[0] = (target, d)

    # 뒤집기
    if is_red:
        group.reverse()

    # 다음 해당 위치에 추가
    state[nx][ny].extend(group)

    # 움직임 이후 같은 공간에 4개 이상이 존재한다면 끝 아니면 계속 진행
    if len(state[nx][ny]) >= 4:
        return True
    return False


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)] # 흰색, 빨간색, 파란색을 나타내는 격자판
state = [[[] for _ in range(N)] for _ in range(N)] # 격자판 내 말들의 위치 및 방향을 파악하는 상태 격자판
# 우좌상하
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(1, K + 1):
    x, y, d = map(int, input().split())
    state[x - 1][y - 1].append((i, d - 1))

turn = 1
found = False
while turn < 1000:
    for i in range(1, K + 1):
        x, y, d, idx = search(i) # 각 좌표, 방향, 여러 말이 있을 때의 위치 즉, index
        if move(x, y, d, idx, i):
            found = True
            break

    if found:
        break

    turn += 1
if found:
    print(turn)
else:
    print(-1)