def gcd(A, B):
    if B == 0:
        return A
    else:
        return gcd(B, A%B)

A = 28
B = 14

print gcd(A, B)