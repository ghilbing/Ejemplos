def uniquePathsWithObstacles(A):
    m = len(A)
    n = len(A[0])
    dp = [1] + [0] * (n-1)

    for i in range(m):
        for j in range(n):
            if A[i][j] == 1:
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j-1]
    return dp[n-1]


#A = [[1,0]]
A = [[0,0,0],[0,1,0],[0,0,0]]

print uniquePathsWithObstacles(A)