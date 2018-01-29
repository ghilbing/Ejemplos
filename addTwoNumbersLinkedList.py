# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        carry = 0
        temp = n = ListNode(0)
        while A or B or carry:
            val1 = val2 = 0
            if A:
                val1 = A.val
                A = A.next
            if B:
                val2 = B.val
                B = B.next
            carry, value = divmod(val1+val2+carry, 10)
            n.next = ListNode(value)
            n = n.next
        return temp.next
