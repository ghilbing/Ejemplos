def createBinaryTree(A):
    if A is None:
        return False
    if len(A) == 1:
        return 0
    if len(A)>=1:
        node = A[1]
        queue= []
        queue.append(node)
        count = 1
        while (count < len(A) or len(queue) < 0):
            node.left = A[count+1]
            queue.append(node)
            if (count < len(A)):
                node.right = A[count+1]
            queue.append(node.right)
    return node





A = [10, 7, 14, 20, 1, 5, 8]

print createBinaryTree(A)