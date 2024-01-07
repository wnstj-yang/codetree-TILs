N = int(input())
numbers = list(map(int, input().split()))
result = 0
numbers.sort(reverse=True)
for i in range(N):
    num = numbers[i]
    value = num - (i + 1 - 1)
    if value > 0:
        result += value
print(result)