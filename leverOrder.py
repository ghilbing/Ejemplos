# Definition for a  binary tree node
 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        if not A:
            return []
        res = []
        level = [A]
        while level:
            res.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
        return res

    def levelOrder(self, A):
        list = []
        l = deque()
        if A is None:
            return []
        list.append([A.val])
        if A.left is not None:
            l.append(A.left)
        if A.right is not None:
            l.append(A.right)

        while len(l) > 0:
            l2 = []
            # node = l.popleft()
            # l2.append(node.val)
            l1 = deque()
            while len(l) > 0:
                node1 = l.popleft()
                l2.append(node1.val)
                if node1.left is not None:
                    l1.append(node1.left)
                if node1.right is not None:
                    l1.append(node1.right)

            l = l1
            list.append(l2)
        return list