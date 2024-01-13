import re

numbers = input().split('-')
result = []

for number in numbers:
    splitted = list(map(int, number.split('+')))
    result.append(sum(splitted))
print(result[0] - sum(result[1:]))