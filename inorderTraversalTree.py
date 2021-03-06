# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):

        result, stack = [], [(A, False)]

        while stack:
            current, visited = stack.pop()
            if current:
                if visited:
                    result.append(current.val)
                else:
                    stack.append((current.right, False))
                    stack.append((current, True))
                    stack.append((current.left, False))

        return result

def inorderTraversalFastest(A):
    stack = []
    node = A
    res = []
    while len(stack) > or node is not None:
        if node is not None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            res.append(node.val)
            node = node.right
    return res