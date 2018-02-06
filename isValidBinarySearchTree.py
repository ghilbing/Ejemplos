def isValidBST(A):
    output = []
    self.inOrder(A, output)

    for i in range(1, len(output)):
        if output[i - 1] >= output[i]:
            return 0
    return 1


def inOrder(self, A, output):
    if A is None:
        return
    self.inOrder(A.left, output)
    output.append(A.val)
    self.inOrder(A.right, output)


def isValidBSTII(self, root):
    if not root:
        return True
    stack = []
    res = []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            res.append(root.val)
            root = root.right
    if res == sorted(res) and len(res) == len(set(res)):
        return True
    else:
        return False
