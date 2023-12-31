N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
result = numbers[-1]
for i in range(N - 1):
    num = numbers[i]
    result += num / 2
print(round(result, 1))