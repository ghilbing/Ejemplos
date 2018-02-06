def singleNumber(A):
    res = 0
    for num in A:
        res ^= num
    return res

A = [1, 2, 3, 2, 1]

print singleNumber(A)