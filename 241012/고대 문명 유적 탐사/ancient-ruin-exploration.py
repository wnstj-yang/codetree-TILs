from collections import deque


def rotate(i, j, source_arr, new_arr):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            ox, oy = x - i, y - j  # 우선 0,0 부터 좌표를 초기화
            rx, ry = oy, j + 3 - 1 - ox
            new_arr[rx + i][ry] = source_arr[x][y]
    return new_arr


def rotate_check(i, j):
    copy_board_90 = [item[:] for item in board]
    max_x = i + 3
    max_y = j + 3
    cx, cy = (i + max_x) // 2, (j + max_y) // 2
    max_candidate = [0, 90, cy, cx]
    # print(cx, cy)
    max_list = []
    rotate(i, j, board, copy_board_90)

    copy_board_90 = rotate(i, j, board, copy_board_90)
    result, result_list = check_product(copy_board_90)
    if result > max_candidate[0]:
        max_candidate = [result, 90, cy, cx]
        max_list = result_list
    # print('90도')
    # for z in copy_board_90:
    #     print(z)

    # 180도 회전했을 때
    copy_board_180 = [item[:] for item in copy_board_90]
    copy_board_180 = rotate(i, j, copy_board_90, copy_board_180)
    result, result_list = check_product(copy_board_180)
    if result > max_candidate[0]:
        max_candidate = [result, 180, cy, cx]
        max_list = result_list
    # print('180도')
    # for z in copy_board_180:
    #     print(z)
    # 270도 회전했을 때
    copy_board_270 = [item[:] for item in copy_board_180]
    copy_board_270 = rotate(i, j, copy_board_180, copy_board_270)
    result, result_list = check_product(copy_board_270)
    if result > max_candidate[0]:
        max_candidate = [result, 270, cy, cx]
        max_list = result_list
    # print('270도')
    # for z in copy_board_270:
    #     print(z)
    max_candidate.append(max_list)
    return max_candidate


# 유물 1차 획득
def check_product(arr):
    visited = [[False] * 5 for _ in range(5)]
    total = 0
    total_list = []
    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                num = arr[i][j]
                cnt = 1
                cnt_list = [(i, j)]
                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                            continue
                        if not visited[nx][ny] and arr[nx][ny] == num:
                            q.append((nx, ny))
                            visited[nx][ny] = True
                            cnt_list.append((nx, ny))
                            cnt += 1
                if cnt >= 3:
                    total_list.extend(cnt_list)
                    total += cnt
    # print(total, total_list)
    return [total, total_list]


# 5x5격자이기에 고정이므로 좌표값도 고정가능

K, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(5)]
add_list = list(map(int, input().split()))
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
total_result = []
for o in range(K):
    # print(o, '번')
    max_result = []
    for x in range(3):
        for y in range(3):
            result = rotate_check(x, y)
            if result[0] != 0:
                max_result.append(result)
    # for z in board:
    #     print(z)
    # print('---')
    if len(max_result) > 0:
        max_result.sort(key=lambda x: (-x[0], x[1], x[2], x[3]))
        val, d, cy, cx, max_list = max_result[0]
        # print(max_result)
        # print(d // 90)
        for _ in range(d // 90):
            copy_board = [item[:] for item in board]
            board = rotate(cx - 1, cy - 1, board, copy_board)
        max_list.sort(key=lambda x: (x[1], -x[0]))
        # print(add_list)
        # print(max_list)
        # print('회전과 1차까지 돈 이후', val, d, cx, cy)
        # for z in board:
        #     print(z)
        # print('---')
        for x, y in max_list:
            new_val = add_list.pop(0)
            board[x][y] = new_val
        add_cnt = val
        # for z in board:
        #     print(z)
        # print('---')
        while True:
            result, result_list = check_product(board)
            # print(add_cnt)
            # print(result, result_list)
            if result == 0:
                # print('탈출', result, result_list)
                break
            add_cnt += result
            result_list.sort(key=lambda x: (x[1], -x[0]))
            # print(add_list)
            # print(result_list)
            for x, y in result_list:
                if add_list:
                    new_val = add_list.pop(0)
                    board[x][y] = new_val
            # for z in board:
            #     print(z)
            # print('---')
        total_result.append(add_cnt)
    else:
        break

print(*total_result)