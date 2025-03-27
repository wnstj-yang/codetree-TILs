from collections import deque

def is_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


def get_groups():
    visited = [[False] * N for _ in range(N)]
    groups = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                number = board[i][j]
                coors = [(i, j)]
                q = deque()
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if is_range(nx, ny) and not visited[nx][ny] and number == board[nx][ny]:
                            coors.append((nx, ny))
                            q.append((nx, ny))
                            visited[nx][ny] = True
                groups.append([number, coors])
    return groups


def harmony_groups(idx, cnt):
    global total

    if cnt == 2:
        first, second = all_groups[pair_group[0]], all_groups[pair_group[1]]
        contacted = 0
        f_num, s_num = first[0], second[0]
        f_list, s_list = first[1], second[1]
        for x, y in f_list:
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if is_range(nx, ny) and (nx, ny) in s_list:
                    contacted += 1
        total += ((len(f_list) + len(s_list)) * f_num * s_num * contacted)
        return

    for i in range(idx, len(all_groups)):
        if not group_visited[i]:
            group_visited[i] = True
            pair_group[cnt] = i
            harmony_groups(i + 1, cnt + 1)
            group_visited[i] = False


def rotate():
    new_board = [[0] * N for _ in range(N)]
    # 왼쪽 위 회전
    for i in range(N // 2):
        for j in range(N // 2):
            new_board[j][N // 2 - 1 - i] = board[i][j]

    # 오른쪽 위 회전
    for i in range(N // 2):
        for j in range(N // 2 + 1, N):
            new_board[j - (N // 2 + 1)][N - 1 - i] = board[i][j]

    # 왼쪽 아래 회전
    for i in range(N // 2 + 1, N):
        for j in range(N // 2):

            new_board[(N // 2 + 1) + j][N - i - 1] = board[i][j]

    # 오른쪽 아래 회전
    idx = 0
    for i in range(N // 2 + 1, N):
        for j in range(N // 2 + 1, N):
            new_board[j][N - 1 - idx] = board[i][j]
        idx += 1

    # 십자 모양 회전
    for i in range(N):
        new_board[N // 2][i], new_board[N - 1 - i][N // 2] = board[i][N // 2], board[N // 2][i]
    return new_board


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
total = 0

for _ in range(4):
    all_groups = get_groups()
    pair_group = [0] * 2
    group_visited = [False] * len(all_groups)

    harmony_groups(0, 0)
    board = rotate()

print(total)
