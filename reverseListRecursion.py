def reverseListRecursion(A):
    if A == None or A.next == None:
        return A
    node = reverseList(A.next)
    A.next.next = A
    A.next = None
    return node

def reverseListIterative(A):
    last = None
    while A:
        next = A.next
        A.next = last
        last = A
        A = next
    return last