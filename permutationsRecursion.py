def permute(A):
    n = len(A)
    if n <= 1:
        return [A]
    res = []
    for i in range(n):
        s = A[:i] + A[i+1:]
        p = permute(s)
        for x in p:
            res.append(A[i:i+1] + x)
    return res

A = [1, 2, 3]


def permuteII(A):
    res = []
    l = 0
    r = len(A) - 1

    def helper(a, l, r, res):
        if l == r:
            k = a[::]
            res.append(k)
        else:
            for i in range(l, r + 1):
                a[l], a[i] = a[i], a[l]
                helper(a, l + 1, r, res)
                a[l], a[i] = a[i], a[l]

    helper(A, l, r, res)
    return res

print permuteII(A)