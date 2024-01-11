N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
if N < 3:
    print(numbers[-1])
else:
    result = numbers[0] + numbers[-1]
    for num in numbers[::-1]:
        if num + numbers[0] == numbers[-1]:
            result = num + numbers[0]
            break
    print(result)