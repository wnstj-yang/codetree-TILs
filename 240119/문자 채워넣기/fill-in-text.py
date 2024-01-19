N = int(input())
target = list(map(str, input().split()))
count_a, count_b = target.count('a'), target.count('b')

cnt = 1
now = target[0]
for t in target[1:]:
    if now != t:
        cnt += 1
        now = t
print((cnt + 2) // 2)