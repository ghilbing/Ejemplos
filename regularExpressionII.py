def isMatch(A, B):
    table = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]
    table[0][0] = 1
    for i in range(2, len(B) + 1):
        table[i][0] = table[i - 2][0] and B[i - 1] == '*'

    for i in range(1, len(B) + 1):
        for j in range(1, len(A) + 1):
            if B[i - 1] != '*':
                table[i][j] = int(table[i - 1][j - 1] and (B[i - 1] == A[j - 1] or B[i - 1] == '.'))

            else:
                table[i][j] = int(table[i - 2][j] or table[i - 1][j])
                if B[i - 2] == A[j - 1] or B[i - 2] == '.':
                    table[i][j] |= table[i][j - 1]

    return table[-1][-1]


A = "a"
B = "a"

print isMatch(A,B)

#----------------------------------------

def isMatchII(A, B):
    # base case length = 0

    dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
    dp[0][0] = 1

    for i in range(1, len(B) + 1):
        if B[i - 1] == '*':
            dp[0][i] = dp[0][i - 1] or dp[0][i - 2]

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1] or B[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif B[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]
                if dp[i][j] != 1:
                    if A[i - 1] == B[j - 2] or B[j - 2] == '.':
                        dp[i][j] = dp[i - 1][j - 1] or dp[i][j - 1] or dp[i - 1][j]

    return dp[-1][-1]
