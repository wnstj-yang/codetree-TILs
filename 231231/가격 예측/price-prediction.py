n, w = map(int, input().split())
prices = []
for _ in range(n):
    prices.append(int(input()))
buy, sell = prices[0], prices[0]
if n > 1:
    for i in range(1, n):

        if sell < prices[i] or i == n - 1:
            sell = prices[i]

            if i == n - 1:
                if buy < sell:
                    stocks = w // buy
                    left = w % buy
                    w = (stocks * sell) + left
                break
        # print(buy, sell, prices[i])
        if sell >= prices[i]:
            if buy != sell:

                stocks = w // buy
                left = w % buy
                w = (stocks * sell) + left

                buy = prices[i]
            sell = prices[i]

        if buy > prices[i]:
            buy = prices[i]
        
print(w)