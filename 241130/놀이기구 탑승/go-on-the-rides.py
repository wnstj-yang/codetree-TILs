def is_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


def search(student, likes):
    candidates = []
    for x in range(N):
        for y in range(N):
            if board[x][y] == 0:
                like, empty = 0, 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if is_range(nx, ny):
                        if board[nx][ny] == 0:
                            empty += 1
                        elif board[nx][ny] in students[student]:
                            like += 1
                candidates.append([like, empty, x, y])
    if candidates:
        candidates.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
        x, y = candidates[0][2], candidates[0][3]
        board[x][y] = student

score = {
    0: 0,
    1: 1,
    2: 10,
    3: 100,
    4: 1000
}
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = int(input())
board = [[0] * N for _ in range(N)]
length = N * N
total = 0
students = {}
for _ in range(N * N):
    n0, n1, n2, n3, n4 = list(map(int, input().split()))
    students[n0] = [n1, n2, n3, n4]

for student, likes in students.items():
    search(student, likes)

for x in range(N):
    for y in range(N):
        likes = students[board[x][y]]
        cnt = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if is_range(nx, ny) and board[nx][ny] in likes:
                cnt += 1
        total += score[cnt]
print(total)
