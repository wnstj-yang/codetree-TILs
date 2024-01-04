N = int(input())
nums = {}
result = 0
for _ in range(N):
    x, y = map(int, input().split())
    if x not in nums:
        nums[x] = y
    else:
        if nums[x] != y:
            nums[x] = y
            result += 1
print(result)