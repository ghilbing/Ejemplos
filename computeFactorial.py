def factorial(A):
    if A <= 1:
        return 1
    else:
        A = A * factorial(A-1)
    return A

A = 6

print factorial(A)