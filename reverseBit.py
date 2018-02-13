def reverse(A):
    res = 0
    for i in range(32):
        res <<= 1
        res = res | (A & 1)
        A >>= 1
    return res

A = 546463

print reverse(A)