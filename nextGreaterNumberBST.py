def nextSuccesor(A, B):
    succesor = None
    while A:
        if B < A.val:
            succesor = A
            A = A.left
        else:
            A = A.right
    return succesor



