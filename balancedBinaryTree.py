def isBalanced(A):
    def balance(A):
        if A is None:
            return 0
        left = balance(A.left)
        right = balance(A.right)
        if left == -1 or right == 1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    if balance(A) != -1:
        return 1
    else:
        return 0