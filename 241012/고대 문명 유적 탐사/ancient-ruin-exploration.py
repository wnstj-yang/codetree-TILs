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
    max_list = []
    rotate(i, j, board, copy_board_90)

    copy_board_90 = rotate(i, j, board, copy_board_90)
    result, result_list = check_product(copy_board_90)
    if result > max_candidate[0]:
        max_candidate = [result, 90, cy, cx]
        max_list = result_list

    # 180도 회전했을 때
    copy_board_180 = [item[:] for item in copy_board_90]
    copy_board_180 = rotate(i, j, copy_board_90, copy_board_180)
    result, result_list = check_product(copy_board_180)
    if result > max_candidate[0]:
        max_candidate = [result, 180, cy, cx]
        max_list = result_list

    # 270도 회전했을 때
    copy_board_270 = [item[:] for item in copy_board_180]
    copy_board_270 = rotate(i, j, copy_board_180, copy_board_270)
    result, result_list = check_product(copy_board_270)
    if result > max_candidate[0]:
        max_candidate = [result, 270, cy, cx]
        max_list = result_list

    max_candidate.append(max_list)
    return max_candidate


# 유물 획득
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
    return [total, total_list]


K, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(5)]
add_list = list(map(int, input().split()))
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
total_result = []
for o in range(K):
    max_result = []
    for x in range(3):
        for y in range(3):
            result = rotate_check(x, y)
            if result[0] != 0:
                max_result.append(result)

    if len(max_result) > 0:
        max_result.sort(key=lambda x: (-x[0], x[1], x[2], x[3]))
        val, d, cy, cx, max_list = max_result[0]

        for _ in range(d // 90):
            copy_board = [item[:] for item in board]
            board = rotate(cx - 1, cy - 1, board, copy_board)
        max_list.sort(key=lambda x: (x[1], -x[0]))

        for x, y in max_list:
            new_val = add_list.pop(0)
            board[x][y] = new_val
        add_cnt = val

        while True:
            result, result_list = check_product(board)
            if result == 0:
                break
            add_cnt += result
            result_list.sort(key=lambda x: (x[1], -x[0]))
            for x, y in result_list:
                if add_list:
                    new_val = add_list.pop(0)
                    board[x][y] = new_val
        total_result.append(add_cnt)
    else:
        break

print(*total_result)