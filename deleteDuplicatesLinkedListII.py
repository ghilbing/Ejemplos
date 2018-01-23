# Definition for singly-linked list.
 class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        p=None
        r=ListNode(0)
        dummy=r
        prev=None
        while A!=None:
            if A.val!=p:
                prev=r
                r.next=ListNode(A.val)
                r=r.next
            else:
                if r.val==p:
                    prev.next=None
                    r=prev
            p=A.val
            A=A.next
        return dummy.next