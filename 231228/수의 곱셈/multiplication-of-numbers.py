numbers = list(map(int, input().split()))
odds = []
evens = []
for i in range(2):
    for j in range(i + 1, 3):
        number = numbers[i] * numbers[j]
        if number not in numbers:
            numbers.append(number)
numbers.append(numbers[0] * numbers[1] * numbers[2])
numbers.sort(reverse=True)
result = 0
for num in numbers:
    result = num
    if num % 2:
        break
print(result)