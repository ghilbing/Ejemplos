def pathSumBST(A, B):
    suma = 0
    while A and suma < B:
        if B < A.val and suma < B:
            suma = suma + A.val
            A = A.left
        else:
            A = A.right
    if suma == B:
        return 1
    else:
        return 0

#Another solution

def pathSumBSTII(A, B):
    suma = B
    if not A:
        return 0
    if not A.left and not A.right and A.val == suma:
        return 1
    suma -= A.val

    return pathSumBSTII(A.left, suma) or pathSumBSTII(A.right, suma)