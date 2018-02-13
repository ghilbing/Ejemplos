#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the root node in the tree
    def sortedListToBST(self, A):
        if not A:
            return
        if not A.next:
            return TreeNode(A.val)
        left = A
        right = A.next.next
        while right and right.next:
            right = right.next.next
            left = left.next
        tmp = left.next
        left.next = None
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(A)
        root.right = self.sortedListToBST(tmp.next)
        return root
