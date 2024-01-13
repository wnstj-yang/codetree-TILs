first, second = list(map(str, input().split()))
first_cnt = first.count('1')
second_cnt = second.count('1')
cnt = 0
for i in range(len(first)):
    if first[i] != second[i]:
        cnt += 1
# 규칙 상으로는 1의 개수를 각각 구하고 뺀 값이 서로 교환하는 조건
# 하나씩 바꾸는 것이 다른 조건
# 이 둘을 합한 것의 2로 나눈 것이 답
# 규칙은 이렇지만 명확한 설명은 모르겠다..
print((cnt + abs(first_cnt - second_cnt)) // 2)