def preOrderTraversal(A):
    stack = []
    ans = []
    root = A
    if root is None:
        return []
    while stack or root:
        if root:
            ans.append(root.val)
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            root = root.right
    return ans
