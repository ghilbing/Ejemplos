import sys


def minPathSum(A):
    m = len(A)
    n = len(A[0])
    dp = [0] + [sys.maxint] * (n-1)

    for i in range(m):
        dp[0] = dp[0] + A[i][0]
        for j in range(1, n):
            dp[j] = min(dp[j-1], dp[j]) + A[i][j]
    return dp[-1]

A = [[1,3,2], [4,3,1], [5,6,1]]

print minPathSum(A)