def romanToInteger(A):
    values = {'I': 1, 'V': 5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    for i in range(len(A)):
        if i > 0 and values[A[i]] > values[A[i-1]]:
            decimal += values[A[i]] - 2 * values[A[i-1]]
        else:
            decimal += values[A[i]]
    return decimal

A = "XXX"
print romanToInteger(A)