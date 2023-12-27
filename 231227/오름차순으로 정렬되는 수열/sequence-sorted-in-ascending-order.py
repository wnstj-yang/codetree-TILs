N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
min_val = numbers[-1]
result = 0
for i in range(N - 1, -1, -1):
    if numbers[i] > min_val:
        if i + 1 < N and numbers[i] == numbers[i + 1]:
            continue
        result += 1
    elif numbers[i] < min_val:
        min_val = numbers[i]
        result += 1
print(result - 1)