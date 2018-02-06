def invertBinaryTreeRecursive(self, A):
    if A:
        mirror = self.invertBinaryTreeRecursive
        A.left = mirror(A.right)
        A.right = mirror(A.left)
    return A

def invertBinaryTreeIterative(A):
    stack = [A]
    while stack:
        node = stack.pop()
        if node:
            temp = node.left
            node.left = node.right
            node.right = temp
            stack.extend([node.right, node.left])
        return A
