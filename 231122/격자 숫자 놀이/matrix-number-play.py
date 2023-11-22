# 2023-11-22
# 21:45 ~ 23:00


def operate_row():
    global m

    for i in range(100):
        cnt_nums = {}
        for j in range(100):
            # 숫자와 개수에 대한 딕셔너리
            if board[i][j]:
                if board[i][j] not in cnt_nums:
                    cnt_nums[board[i][j]] = 1
                else:
                    cnt_nums[board[i][j]] += 1
        # 정렬할 것이 있는지 확인
        if len(cnt_nums) > 0:
            # 출현 빈도 수, 숫자 순으로 오름차순 정렬 진행
            sorted_nums = sorted(cnt_nums.items(), key=lambda x:(x[1], x[0]))
            col = 0 # 새로 넣을 열의 변수
            # 현재 행에서 정렬된 숫자와 출현 횟수를 하나씩 넣어간다.
            for k in range(len(sorted_nums)):
                board[i][col] = sorted_nums[k][0]
                board[i][col + 1] = sorted_nums[k][1]
                col += 2 # 2개의 값을 넣었으므로 인덱스 증가
                # 100을 넘어가는 경우 버린다.
                if col >= 100:
                    break
            m = max(m, col) # 열의 최대 값 갱신
            # 기존에 있었던 값들을 다시 0으로 갱신
            for k in range(col, 100):
                board[i][k] = 0


def operate_col():
    global n

    # 순회할 때 열에서부터 행으로 진행하기 때문에 인덱스 값 변경
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
# 인덱스 상으로 보았을 때 1씩 줄인다.
r -= 1
c -= 1
n, m = 3, 3
board = [[0] * 100 for _ in range(100)]
first = [list(map(int, input().split())) for _ in range(3)] # 첫 3x3 격자판의 값
for i in range(3):
    for j in range(3):
        board[i][j] = first[i][j]
time = 0
while True:
    if board[r][c] == k:
        break

    if n >= m:
        operate_row()
    else:
        operate_col()
    time += 1
    # 못찾는 경우 끝
    if time > 100:
        time = -1
        break
print(time)