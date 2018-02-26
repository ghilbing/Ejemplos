def maxProfit(A):
    max_profit = 0
    min_price = float('inf')
    for price in A:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit


A = [1,2,3,4,2,4,5]
print maxProfit(A)
