def findMinXor(A):
    res = []
    value = 0
    A.sort()
    for i in range(0, len(A) - 1):
        value = A[i] ^ A[i + 1]
        res.append(value)
    res.sort()
    return res[0]


def findMinXorII(A):
    A.sort()
    min_xor = A[0] ^ A[1]
    # min is always achieved by two neighbours in sorted array
    for i in xrange(len(A) - 1):
        min_xor = min(min_xor, A[i] ^ A[i + 1])
    return min_xor


A = [1,3, 4, 5, 6, 7]
print findMinXor(A)