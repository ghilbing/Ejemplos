def solve(A,B):
    dp = [[0 for _ in range(A + 1)] for _ in range(B + 1)]

    # dp(i, j) = number of j digit numbers that can make number i
    # dp(i, 0) = 0 if i != 0
    # dp(0, j) = 0 if i != 0
    # dp(i, j) = sum(dp(i - (1 to 9), j - 1)) + dp[i][j-1] (for 0)

    dp[0][0] = 1
    for i in range(1, B + 1):
        for j in range(1, A + 1):
            running_sum = 0
            for k in range(i - 9, i):
                if k < 0:
                    continue
                else:
                    running_sum += dp[k][j - 1]
            dp[i][j] = running_sum + dp[i][j - 1]
    return dp[-1][-1] % 1000000007

A = 3
B = 6

print solve(A,B)