from collections import deque

# 범위 체크
def is_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True

# 맨해튼 거리
def calulate_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


# 1. 메두사의 이동
# 공원으로 갈 수 없을 수도 있음
def move_medusa():
    global sr, sc

    min_dist = 987654321
    min_d = 0
    for i in range(4):
        nx = sr + dx[i]
        ny = sc + dy[i]
        if is_range(nx, ny):
            dist = calulate_dist(nx, ny, er, ec)
            if dist < min_dist:
                min_d = i
                min_dist = dist
    # 1. 메두사의 이동
    sr = sr + dx[min_d]
    sc = sc + dy[min_d]
    # 2. 이동한 이후 전사가 있으면 잡는다
    if (sr, sc) in knights:
        cnt = 0 # 이동한 위치에 전사의 수 만큼 공격하여 사라지게 한다
        for x, y in range(len(knights)):
            if (x, y) == (sr, sc):
                cnt += 1
        for _ in range(cnt):
            knights.remove((sr, sc))
        knight_board[sr][sc] = 0

# 메두사의 시선
def search(standard):
    directions = direcs[d]
    # TODO: 여기가 중요한 것 같은데 아이디어랑 구현이 좀 어렵네ㅔ;;
    pass


# 2. 전사들의 이동
# 돌로 안변한 전사들만 이동하며 최대 두 칸까지 이동 가능... 같은 칸 공유 가능

# 상하좌우 우선순위 + 대각선
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]
# 두 칸 이동할 수 있는 경우 고려한 좌우상하 우선순위
kx = [0, 0, -1, 1]
ky = [-1, 1, 0, 0]

# 방향에 따라 대각선 표시
direcs = {
    0: [4, 5],
    1: [5, 6],
    2: [6, 7],
    3: [4, 7],
}

N, M = map(int, input().split())
sr, sc, er, ec = map(int, input().split())
k_coors = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]
knights = []
knight_board = [[0] * N for _ in range(N)] # 기사의 개수로 판단
stunned = [] # 돌로 변하게 된 상태
for i in range(0, M, 2):
    x, y = k_coors[i], k_coors[i + 1]
    knights.append((x, y))
print(sr, sc)
move_medusa()
print(sr, sc)
# 해당 턴에서 모든 전사가 이동한 거리 합, 메두사로 인해 돌이 된 전사 수, 메두사를 공격한 전사의 수

