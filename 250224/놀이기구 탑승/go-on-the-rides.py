from collections import deque

def is_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


def put_student(number, favor_list):
    # 1. 비어 있는 공간에서 4방향 돌면서 좋아하는 친구, 빈 공간을 카운팅한다.
    # 2. 빈 공간은 행, 열 좌표도 추가
    result = []
    for x in range(N):
        for y in range(N):
            if board[x][y] == 0:
                favor_cnt, empty_cnt = 0, 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if is_range(nx, ny):
                        if board[nx][ny] in favor_list:
                            favor_cnt += 1
                        if board[nx][ny] == 0:
                            empty_cnt += 1
                result.append((favor_cnt, empty_cnt, x, y))
    result.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
    x, y = result[0][2], result[0][3]
    board[x][y] = number


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
score = {
    0: 0, 1: 1, 2: 10, 3: 100, 4: 1000
}
N = int(input())
board = [[0] * N for _ in range(N)]
students = {}
for _ in range(N * N):
    info = list(map(int, input().split()))
    students[info[0]] = info[1:]
    put_student(info[0], info[1:])

ans = 0
for x in range(N):
    for y in range(N):
        cnt = 0
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if is_range(nx, ny) and board[nx][ny] in students[board[x][y]]:
                cnt += 1
        ans += score[cnt]
print(ans)
