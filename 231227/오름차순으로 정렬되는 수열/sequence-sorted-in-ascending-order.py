N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
target = sorted(numbers)
result = 0
for i in range(N):
    if target[i] != numbers[i]:
        result += 1
print(result - 1)