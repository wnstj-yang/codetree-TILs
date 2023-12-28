N = int(input())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
result = 0
for i in range(0, N, 3):
    num = numbers[i:i+3]
    # print(num)
    if len(num) == 3:
        num.pop(num.index(min(num)))
        result += sum(num)
    else:
        result += sum(num)
print(result)