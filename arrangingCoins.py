def arrangingCoins(A):
    n = A[0]
    for i in range(1, len(A)):
        coins = A[i]
        rows = 0
        j = 0
        while j < coins:
                coins -=j+1
                rows = rows + 1
                j +=1
        print rows




A = [4, 2, 5, 8, 3, 12, 18]

print arrangingCoins(A)