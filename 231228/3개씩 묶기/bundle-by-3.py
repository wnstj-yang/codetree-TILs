N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
result = 0
for i in range(0, N, 3):
    num = numbers[i:i+3]
    if len(num) == 3:
        result += sum(num[1:])
    else:
        result += sum(num)
print(result)