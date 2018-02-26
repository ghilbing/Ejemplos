def maxProfit(A):
    n = len(A)

    if n < 2:
        return 0

    starting_price = A[0]

    max_profits = []
    max_profit = 0

    for price in A:
        if price - starting_price > max_profit:
            max_profit = price - starting_price
        if price < starting_price:
            starting_price = price

        max_profits.append(max_profit)

    max_profit = 0
    ending_price = A[-1]

    for i in xrange(n - 2, -1, -1):
        if ending_price - A[i] + max_profits[i] > max_profit:
            max_profit = ending_price - A[i] + max_profits[i]
        if A[i] > ending_price:
            ending_price = A[i]

    return max_profit

    

A = [1,2,1,2,8,6,5,3,8]

print maxProfit(A)