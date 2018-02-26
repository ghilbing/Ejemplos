def chordCnt(A):
    n = 2 * A
    dpArray = [0] * (n+1)
    dpArray[0] = 1
    dpArray[2] = 1
    for i in range(4, n+1, 2):
        for j in range(0, i-1, 2):
            dpArray[i] += (dpArray[j]*dpArray[i-2-j])
    return int(dpArray[n])%((10**9)+7)

A = 19


def chordCntII(A):
    MODU = 10 ** 9 + 7

    ''' Store numbers of ways to draw chords with 2*n points'''
    dp = [0] * (A + 1)
    dp[0] = 1
    for n in range(1, A + 1):
        # Pick first point as source of first chord.
        # We must leave an even numbers of points.
        res = 0
        for i in range(n):
            res += dp[i] * dp[n - 1 - i]
            res %= MODU
        dp[n] = res

    return dp[A]

print chordCnt(A)
print chordCntII(A)