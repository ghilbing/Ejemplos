def mergeTwoSortedLists(A, B):
    temp = cur = ListNode(0)
    while A and B:
        if A.val < B.val:
            cur.next = A
            A = A.next
        else:
            cur.next = B
            B = B.next
        cur = cur.next
    cur.next = A or B
    return temp.next








class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
