def isRotation(A, B):
    for n in range(len(A)):
        c = c = A[-n:] + A[:-n]
        if B == c:
            return True
    return False

A = [1,2,3,4,5,6,7]
B = [5,6,7,1,2,3,4]

print isRotation(A,B)