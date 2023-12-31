n, w = map(int, input().split())
prices = []
for _ in range(n):
    prices.append(int(input()))
buy, sell = prices[0], prices[0]
if n > 1:
    for i in range(1, n):
        if buy > prices[i]:
            buy = prices[i]

        if sell < prices[i] or i == n - 1:
            sell = prices[i]
            stocks = w // buy
            left = w % buy
            w = (stocks * sell) + left
            buy = prices[i]
print(w)