class Treenode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, A):
        def dfs(node):
            left = right = 0
            leftsum = rightsum = None
            if node.left:
                left, leftsum = dfs(node.left)
                left = max(left, 0)
            if node.right:
                right, rightsum = dfs(node.right)
                right = max(right, 0)
            return node.val + max(left, right), max(node.val + left + right, leftsum, rightsum)


        if A:
            return dfs(A)[1]
        return 0

if __name__ == "__main__":
    A = Treenode(1)
    A.left = Treenode(2)
    A.right = Treenode(3)
    A.left.left = Treenode(4)
    A.right.right = Treenode(5)
    A.right.left = Treenode(6)
    A.left.right = Treenode(7)

print Solution().maxPathSum(A)