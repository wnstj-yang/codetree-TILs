N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
if N == 1:
    print(numbers[0])
elif N == 2:
    print(sum(numbers))
else:
    result = numbers[0] + numbers[-1]
    for i in range(1, N // 2):
        calculate = numbers[i] + numbers[-i - 1]
        if calculate > result:
            result = calculate
    print(result)