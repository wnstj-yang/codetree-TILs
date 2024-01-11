N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
if N < 3:
    print(numbers[-1])
else:
    print(numbers[0] + numbers[-1])