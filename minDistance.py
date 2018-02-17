def minDistance(A, B):
    l1 = len(A) + 1
    l2 = len(B) + 1
    dp = range(l2)
    pre = 0
    for i in range(1, l1):
        pre = i-1
        dp[0] = i
        for j in range(1, l2):
            buf = dp[j]
            dp[j] = min(dp[j]+1, dp[j-1]+1, pre+(A[i-1]!=B[j-1]))
            pre = buf
    return dp[-1]

A = "Anshuman"
B = "Antihuman"

print minDistance(A,B)


def minDistance(self, A, B):
    dp = [[-1] * len(B) for _ in range(len(A))]
    return self.helper(A, B, len(A) - 1, len(B) - 1, dp)


def helper(self, A, B, i, j, dp):
    if i < 0:
        return j + 1
    if j < 0:
        return i + 1

    if dp[i][j] != -1:
        return dp[i][j]

    if A[i] == B[j]:
        dp[i][j] = self.helper(A, B, i - 1, j - 1, dp)
    else:
        dp[i][j] = 1 + min(
            self.helper(A, B, i - 1, j - 1, dp),
            self.helper(A, B, i - 1, j, dp),
            self.helper(A, B, i, j - 1, dp)
        )
    return dp[i][j]