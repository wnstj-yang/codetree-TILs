N = int(input())
target = list(map(str, input().split()))
count_a, count_b = target.count('a'), target.count('b')
if count_a >= count_b:
    print(count_b)
else:
    print(count_a)