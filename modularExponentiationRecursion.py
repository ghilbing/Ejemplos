def exponentiation(A,B,C):
    def myMod(a, b):
        if a%b<0:
            return (a%b)+b
        else:
            return a%b

    if B == 0:
        return myMod(1, C)
    res = 1
    while B > 0:
        if B%2 ==1:
            res = myMod((res*A), C)
        B >>=1
        A = myMod(A*A, C)
    return res

A = 15
B = 7
C = 2

print exponentiation(A, B, C)