first, second = list(map(str, input().split()))
first_cnt = first.count('1')
second_cnt = second.count('1')
cnt = 0
for i in range(len(first)):
    if first[i] != second[i]:
        cnt += 1
print((cnt + abs(first_cnt - second_cnt)) // 2)