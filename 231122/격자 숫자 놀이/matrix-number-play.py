# 2023-11-22
# 21:45 ~


def operate_row():
    global m

    for i in range(100):
        cnt_nums = {}
        for j in range(100):
            if board[i][j]:
                if board[i][j] not in cnt_nums:
                    cnt_nums[board[i][j]] = 1
                else:
                    cnt_nums[board[i][j]] += 1
        if len(cnt_nums) > 0:
            sorted_nums = sorted(cnt_nums.items(), key=lambda x:(x[1], x[0]))
            col = 0
            for k in range(len(sorted_nums)):
                board[i][col] = sorted_nums[k][0]
                board[i][col + 1] = sorted_nums[k][1]
                col += 2
                if col >= 100:
                    break
            m = max(m, col)
            for k in range(col, 100):
                board[i][k] = 0


def operate_col():
    global n

    for j in range(100):
        cnt_nums = {}
        for i in range(100):
            if board[i][j]:
                if board[i][j] not in cnt_nums:
                    cnt_nums[board[i][j]] = 1
                else:
                    cnt_nums[board[i][j]] += 1
        if len(cnt_nums) > 0:
            sorted_nums = sorted(cnt_nums.items(), key=lambda x:(x[1], x[0]))
            row = 0
            for k in range(len(sorted_nums)):
                board[row][j] = sorted_nums[k][0]
                board[row + 1][j] = sorted_nums[k][1]
                row += 2
                if row >= 100:
                    break
            n = max(n, row)
            for k in range(row, 100):
                board[k][j] = 0




r, c, k = map(int, input().split())
r -= 1
c -= 1
n, m = 3, 3
board = [[0] * 100 for _ in range(100)]
first = [list(map(int, input().split())) for _ in range(3)]
for i in range(3):
    for j in range(3):
        board[i][j] = first[i][j]
time = 0
while True:
    if n >= m:
        operate_row()
    else:
        operate_col()
    time += 1
    if time > 100:
        time = -1
        break
    if board[r][c] == k:
        break
print(time)