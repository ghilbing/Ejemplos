def longestCommonString(A):
    if not A or len(A) == 0:
        return ''

    prefix = A[0]

    for i in range(1, len(A)):
        j = 0
        while j < min(len(A[i]), len(prefix)):
            if A[i][j] != prefix[j]:
                break
            j += 1
        prefix = prefix[:j]
    return prefix


A = ['abcd', 'abde', 'abab']

print longestCommonString(A)
