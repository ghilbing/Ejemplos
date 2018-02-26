def wordBreak(A, B):
    memo = {len(A): ['']}

    def sentences(i):
        if i not in memo:
            memo[i] = [A[i:j] + (tail and ' ' + tail)
                       for j in range(i + 1, len(A) + 1)
                       if A[i:j] in B
                       for tail in sentences(j)]
        return memo[i]

    return sentences(0)

#A = "helloworld"
#B = ["hello", "world"]

A = "catsandog"
B = ["cat", "cats", "and", "sand", "dog"]

print wordBreak(A, B)

