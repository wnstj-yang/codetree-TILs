n, a, d = map(int, input().split())
numbers = list(map(int, input().split()))
length = 0
target = a
for num in numbers:
    if num == target:
        target += d
        length += 1
print(length)