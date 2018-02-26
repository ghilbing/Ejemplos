def minDistnace(A,B):
    l1, l2 = len(A)+1, len(B)+1
    dp = range(l2)
    pre = 0
    for i in range(1, l1):
        pre, dp[0] = i-1, i
        for j in range(1, l2):
            buf = dp[j]
            dp[j] = min(dp[j]+1, dp[j-1]+1, pre + (A[i-1] != B[j-1]))
            pre = buf
    return dp[-1]

A = "holacomoestas"
B = "Cata"

print minDistnace(A,B)


def minDistanceII(A, B):
    dp = [[0 for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]

    for j in range(len(A) + 1):
        dp[0][j] = j

    for j in range(1, len(B) + 1):
        dp[j][0] = j

    for i in range(1, len(B) + 1):
        for j in range(1, len(A) + 1):
            if B[i - 1] == A[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    return dp[-1][-1]


print minDistanceII(A,B)