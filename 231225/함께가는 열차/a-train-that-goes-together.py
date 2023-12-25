N = int(input())
trains = []
result = 0
for _ in range(N):
    loc, speed = map(int, input().split())
    trains.append((loc, speed))
trains.sort(key=lambda x:(x[1]))
min_speed = int(1e9) + 1
for l, s in trains:
    if min_speed >= s:
        min_speed = s
        result += 1
print(result)