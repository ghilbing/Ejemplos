# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        res = []
        temp = []
        pila = [A]
        flag = 1
        if not A:
            return []
        while pila:
            for i in range(len(pila)):
                node = pila.pop(0)
                temp +=[node.val]
                if node.left: pila +=[node.left]
                if node.right: pila +=[node.right]
            res += [temp[::flag]]
            temp = []
            flag *= -1
        return res


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):

        res = []
        if A is None:
            return res

        queue = [A]
        ltr = True  # Left to right
        while queue:
            # Queue is always in BF order, we reverse it on the fly if needed
            res.append(node.val for node in (queue if ltr else reversed(queue)))
            # BF traversal
            queue = [child for node in queue
                     for child in [node.left, node.right]
                     if child is not None]
            ltr = not ltr

        return res