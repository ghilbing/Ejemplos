def insertionSort(A):
    if not A:
        return A

    temp = ListNode(0)
    temp.next = head

    while head and head.next:
        if head.val <= head.next.val:
            head = head.next
        else:
            cur = temp
            while cur.next.val < head.next.val:
                cur = cur.next
            tmp = head.next
            head.next = tmp.next
            tmp.next = cur.next
            cur.next = tmp
    return temp.next

def insertionWithArray(A):
    res = []
    head = A
    while A is not None:
        res.append(A.val)
        A = A.next

    A = head
    res.sort()
    for i in res:
        A.val = i
        A = A.next
    return head