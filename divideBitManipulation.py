def divide(A, B):
    MIN = -2147483648
    MAX = 2147483647
    positive = (A < 0) is (B < 0)
    dividendo = abs(A)
    divisor = abs(B)
    res = 0
    while dividendo >= divisor:
        temp = divisor
        i = 1
        while dividendo >= temp:
            dividendo -= temp
            res += i
            i <<= 1
            temp <<= 1
    if not positive:
        return -res
    return min(max(MIN, res), MAX)

A = 5
B = 2

print divide(A, B)