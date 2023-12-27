N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
target = sorted(numbers)
result = 0
# 변경된 갯수를 카운팅하지만 횟수를 구하므로 마지막에 갯수 - 1 = 횟수로 표시
for i in range(N):
    if target[i] != numbers[i]:
        result += 1
print(result - 1)