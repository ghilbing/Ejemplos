def isValidBinaryTree(A):
    lena = A[0]
    queue = []
    res = []
    MIN = -2**32
    root = MIN
    for value in range(1, lena,2):
        size = A[value]
        for i in range(0,size):
            if A[value] < root:
                res.append("NO")
            else:
                queue.append(A[value+1])
        while len(queue) > 0 and queue[-1] < value:
            root = queue.pop()
            queue.append(A[value])
        res.append("YES")
    return res


















A = [5, 3, 1, 2, 3, 3, 2, 1, 3, 6, 3, 2, 1, 5, 4, 6, 4, 1 ,3 ,4, 2, 5, 3 ,4 ,5 ,1, 2]


print isValidBinaryTree(A)