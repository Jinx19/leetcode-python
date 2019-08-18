

def maxProfit(prices):
    if prices is None or len(prices) <= 1:
        return 0
    profit = 0
    for i in rangΩe(1, len(prices)):
        diff = prices[i] - prices[i - 1]
        if diff > 0:
            profit += diff
    return profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))