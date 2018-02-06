def isSameTree(self, A, B):
    if not A and not B:
        return 1
    if not A or not B:
        return 0
    while A and B:
        if A.left != B.left or A.right != B.right:
            break
        else:
            if A.left.val == B.left.val and A.right.val == B.right.val:
                return 1
    return 0


def isSameTreeRecursiva(A, B):
    if A and B:
        if A.val == B.val and self.isSameTreeRecursiva(A.left, B.left) and self.isSameTreeRecursiva(A.rigth, B.right):
            return 1
        else:
            return 0
        if A is B:
            return 1
        else:
            return 0