def is_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


# 플레이어 움직임
def move_player(number):
    x, y, d, s, g = players[number]  # 좌표(x, y), 방향(d), 초기 능력치(s), 총(g)
    del player_coors[(x, y)]
    nx = x + dx[d]
    ny = y + dy[d]
    if not is_range(nx, ny):
        d = (d + 2) % 4
        nx = x + dx[d]
        ny = y + dy[d]
    # 움직이려는 곳에 플레이어가 없을 경우
    if (nx, ny) not in player_coors:
        if len(gun_board[nx][ny]) > 0:
            strong_gun = max(gun_board[nx][ny])
            strong_gun_idx = gun_board[nx][ny].index(strong_gun)
            if strong_gun > g:
                # 기존에 가지고 있던 총이
                if g > 0:
                    gun_board[nx][ny].append(g)
                g = strong_gun
                gun_board[nx][ny].remove(strong_gun)
        # 플레이어 움직임 좌표 및 정보 갱신
        player_coors[(nx, ny)] = number
        players[number] = [nx, ny, d, s, g]
        # print('플레이어 없음', nx, ny, d, s, g, number)
    # 플레이어가 있는 경우
    else:
        target = player_coors[(nx, ny)]
        tx, ty, td, ts, tg = players[target]
        # print(nx, ny, d, s, g)
        # print(tx, ty, td, ts, tg)
        del player_coors[(nx, ny)]
        if tx != nx and ty != ny:
            return
        diff = abs((s + g) - (ts + tg))
        target_win = False
        if s + g == ts + tg:
            if s < ts:
                target_win = True
        elif s + g < ts + tg:
            target_win = True
        if not target_win:
            score[number] += diff
            # print('진 플레이어', target)
            # print(tx, ty, td, ts, tg)
            # 진 플레이어가 총을 내려 놓음
            if tg > 0:
                gun_board[tx][ty].append(tg)
            tg = 0
            for i in range(4):
                td = (td + i) % 4
                ntx = tx + dx[td]
                nty = ty + dy[td]
                if not is_range(ntx, nty) or (ntx, nty) in player_coors:
                    continue
                # 플레이어가 없으니 빈 칸이기에 움직인다.
                # 움직인 이후 가장 공격력 높은 총 획득
                if len(gun_board[ntx][nty]) > 0:
                    t_strong_gun = max(gun_board[ntx][nty])
                    gun_board[ntx][nty].remove(t_strong_gun)
                    tg = t_strong_gun
                    tx, ty = ntx, nty
                    break
            if len(gun_board[nx][ny]) > 0:
                # 이긴 플레이어의 경우 해당 칸에서 공격력 높은 총 획득
                strong_gun = max(gun_board[nx][ny])
                strong_gun_idx = gun_board[nx][ny].index(strong_gun)
                if strong_gun > g:
                    # 기존에 가지고 있던 총이
                    if g > 0:
                        gun_board[nx][ny].append(g)
                    g = strong_gun
                    gun_board[nx][ny].remove(strong_gun)
            # 이긴, 진 플레이어 좌표 및 정보 갱신
        else:
            score[target] += diff
            if g > 0:
                gun_board[nx][ny].append(g)
            g = 0
            for i in range(4):
                d = (d + i) % 4
                nnx = nx + dx[d]
                nny = ny + dy[d]
                if not is_range(nnx, nny) or (nnx, nny) in player_coors:
                    continue
                # 플레이어가 없으니 빈 칸이기에 움직인다.
                # 움직인 이후 가장 공격력 높은 총 획득
                if len(gun_board[nnx][nny]) > 0:
                    strong_gun = max(gun_board[nnx][nny])
                    gun_board[nnx][nny].remove(strong_gun)
                    g = strong_gun
                    nx, ny = nnx, nny
                    break
            # 이긴 플레이어의 경우 해당 칸에서 공격력 높은 총 획득
            if len(gun_board[tx][ty]) > 0:
                strong_gun = max(gun_board[tx][ty])
                strong_gun_idx = gun_board[tx][ty].index(strong_gun)
                if strong_gun > tg:
                    # 기존에 가지고 있던 총이
                    if tg > 0:
                        gun_board[tx][ty].append(tg)
                    tg = strong_gun
                    gun_board[tx][ty].remove(strong_gun)
        player_coors[(tx, ty)] = target
        players[target] = [tx, ty, td, ts, tg]
        player_coors[(nx, ny)] = number
        players[number] = [nx, ny, d, s, g]


N, M, K = map(int, input().split())
temp_board = [list(map(int, input().split())) for _ in range(N)]
gun_board = [[[] for _ in range(N)] for _ in range(N)]
players = {}
player_coors = {}
score = [0] * M
# 문제의 순서대로 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 총은 한 개 이상이 존재할 수 있기에 따로 만든 gun_board 2차원리스트에 넣는다
for i in range(N):
    for j in range(N):
        if temp_board[i][j] > 0:
            gun_board[i][j].append(temp_board[i][j])

for i in range(M):
    x, y, d, s = map(int, input().split())
    players[i] = [x - 1, y - 1, d, s, 0]
    player_coors[(x - 1, y - 1)] = i

for _ in range(K):
    # 1.플레이어 순서대로 라운드 진행
    for i in range(M):
        move_player(i)
    # print('플레이어', players)
    # print('플레이어 좌표', player_coors)
    # for z in gun_board:
    #     print(z)
    # print('-----------')
print(*score)