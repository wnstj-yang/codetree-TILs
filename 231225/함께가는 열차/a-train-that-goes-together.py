N = int(input())
trains = []
result = 0
for _ in range(N):
    loc, speed = map(int, input().split())
    trains.append((loc, speed))

min_speed = int(1e9) + 1
# 출발점이 뒤에있는 열차 속도가 앞 열차보다 빠른지 판단(뒤집어준다)
for l, s in trains[::-1]:
    if min_speed >= s:
        min_speed = s
        result += 1
print(result)