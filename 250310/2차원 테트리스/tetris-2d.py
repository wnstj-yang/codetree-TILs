def move_block(t, x, y):
    # 1. red 움직임 진행
    j = 1 # 꽉찬 경우도 고려한다면 굳이 0부터 할 필요없다.
    if t == 1 or t == 2:
        while True:
            if j + 1 > 5 or red[x][j + 1]:
                red[x][j] = 1
                if t == 2:
                    red[x][j - 1] = 1
                break
            j += 1
    else:
        while True:
            if j + 1 > 5 or red[x][j + 1] or (x + 1 < 4 and red[x + 1][j + 1]):
                red[x][j], red[x + 1][j] = 1, 1
                break
            j += 1

    # 2. yellow 움직임 진행
    i = 1
    if t == 1 or t == 3:
        while True:
            if i + 1 > 5 or yellow[i + 1][y]:
                yellow[i][y] = 1
                if t == 3:
                    yellow[i - 1][y] = 1
                break
            i += 1
    else:
        while True:
            if i + 1 > 5 or yellow[i + 1][y] or (y + 1 < 4 and yellow[i + 1][y + 1]):
                yellow[i][y], yellow[i][y + 1] = 1, 1
                break
            i += 1


# 연한 부분에 블록이 있으므로 한 칸씩 모두 내려준다
def push_block():
    global score

    # 1. red 제거
    for j in range(2, 6):
        cnt = 0
        for i in range(4):
            if red[i][j]:
                cnt += 1
            else:
                break

        if cnt == 4:
            remove_line(j, 'red')
            score += 1

    # 1.2 red 연한 부분 처리
    for j in range(2):
        for i in range(4):
            if red[i][j]:
                remove_line(5, 'red')

    # 2. yellow 제거
    for i in range(2, 6):
        cnt = 0
        for j in range(4):
            if yellow[i][j]:
                cnt += 1
            else:
                break

        if cnt == 4:
            remove_line(i, 'yellow')
            score += 1

    # 2.2 yellow 연한 부분 처리
    for i in range(2):
        for j in range(4):
            if yellow[i][j]:
                remove_line(5, 'yellow')

# 각 해당 idx부터 1칸씩 줄이기
def remove_line(idx, t='red'):
    # 1. red 밀어주기
    if t == 'red':
        for j in range(idx, 0, -1):
            for i in range(4):
                red[i][j] = red[i][j - 1]
        for i in range(4):
            red[i][0] = 0
    else:
        # 2. yellow 밀어주기
        for i in range(idx, 0, -1):
            for j in range(4):
                yellow[i][j] = yellow[i - 1][j]
        for j in range(4):
            yellow[0][j] = 0


K = int(input())

# 상하좌우
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
yellow = [[0] * 4 for _ in range(6)]
red = [[0] * 6 for _ in range(4)]
score = 0
total = 0
for _ in range(K):
    t, x, y = map(int, input().split())
    move_block(t, x, y)
    push_block()
for r in red:
    total += sum(r)
for y in yellow:
    total += sum(y)
print(score)
print(total)
