N = int(input())
trains = []
result = 0
for _ in range(N):
    loc, speed = map(int, input().split())
    trains.append((loc, speed))

min_speed = int(1e9) + 1
for l, s in trains[::-1]:
    if min_speed >= s:
        min_speed = s
        result += 1
print(result)