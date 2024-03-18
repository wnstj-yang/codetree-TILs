# 2024-03-18


def is_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


def set_student(num):
    candidates = []
    for x in range(N):
        for y in range(N):
            empty = 0
            friends = 0
            if board[x][y] == 0:
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if is_range(nx, ny):
                        if board[nx][ny] == 0:
                            empty += 1
                        elif board[nx][ny] in student_info[num]:
                            friends += 1
                candidates.append([friends, empty, x, y])

    candidates.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    tx, ty = candidates[0][2], candidates[0][3]
    return [tx, ty]


N = int(input())
board = [[0] * N for _ in range(N)]
student_info = {}
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
score = {
    0: 0,
    1: 1,
    2: 10,
    3: 100,
    4: 1000
}
result = 0


for _ in range(N * N):
    info = list(map(int, input().split()))
    student_info[info[0]] = info[1:]


for num in student_info.keys():
    x, y = set_student(num)
    board[x][y] = num


for x in range(N):
    for y in range(N):
        cnt = 0
        num = board[x][y]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if is_range(nx, ny):
                if board[nx][ny] in student_info[num]:
                    cnt += 1
        result += score[cnt]
        
print(result)