def lis(A):
    dp = [1 for _ in range(len(A))]

    for i in range(1, len(A)):
        for j in range(i):
            if A[i] > A[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

print lis(A)