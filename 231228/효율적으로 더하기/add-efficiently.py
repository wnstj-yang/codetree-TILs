N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
result = 0
cnt = 0
for num in numbers:
    cnt += num
    result += cnt
print(result)