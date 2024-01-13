first, second = list(map(str, input().split()))
first_cnt = first.count('1')
second_cnt = second.count('1')
print(abs(first_cnt - second_cnt) + 1)