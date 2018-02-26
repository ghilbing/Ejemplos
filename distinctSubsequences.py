def numDistinct(A, B):
    m = len(A)
    n = len(B)
    dp = [[0] * (n + 1) for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if j == 0:
                dp[i][j] = 1
            elif i > 0 and j > 0:
                dp[i][j] = dp[i - 1][j]
                if A[i - 1] == B[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
    return dp[-1][-1]


A = "rabbbit"
B = "rabbit"


#Better time and speace complexity

def numDistinctII(A,B):
    m = len(A)
    n = len(B)

    dp = [1] * (m+1)

    for j in range(1, n+1):
        for i in range(m+1):
            tmp = dp[i]

            if i == 0:
                dp[i] = 0
            elif i > 0 and j >0:
                dp[i] = dp[i-1]
                if A[i-1] == B[j-1]:
                    dp[i] += prev
            prev = tmp
    return dp[-1]



print numDistinct(A,B)
print numDistinctII(A,B)