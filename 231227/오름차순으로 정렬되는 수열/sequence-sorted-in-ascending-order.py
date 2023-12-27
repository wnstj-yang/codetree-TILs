N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
min_val = numbers[-1]
min_idx = N - 1
target = sorted(numbers)
result = 0
for i in range(N - 1, -1, -1):
    if numbers[i] > min_val:
        if min_idx + 1 < N and numbers[i] == numbers[min_idx + 1]:
            continue
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
        # print(numbers, min_val, min_idx)
        min_val = numbers[i]
        min_idx = i
        result += 1
    # elif numbers[i] < min_val:
    #     min_val = numbers[i]
    #     min_idx = i
    #     result += 1
print(result)