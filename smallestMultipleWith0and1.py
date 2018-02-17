def multiple(A):
    if A < 2:
        return 1
    dp = [0] * A
    i = 0
    while dp[0] == 0:
        x = pow(10, i)
        xmodn = x % A
        if xmodn == 0:
            return x
        dp1 = [0] * A
        dp1[xmodn] = x
        for j in range(A - 1, -1, -1):
            dp1[j] = (dp[(j - xmodn) % A] + x) if dp[(j - xmodn) % A] != 0 else dp1[j]

            for j in range(0, A):
                dp[j] = dp1[j] if dp[j] == 0 else dp[j]
            i += 1
    return dp[0]

A = 55

print multiple(A)