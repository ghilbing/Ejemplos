def anytwo(A):
    n = len(A)
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1,n):
        for j in range(1,n):
            if A[i-1] == A[j-1] and i != j:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    return dp[n-1][n-1]


A = "abba"

print anytwo(A)