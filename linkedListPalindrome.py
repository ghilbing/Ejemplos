def lPalin(self, A):
    if A is None:
        return 0
    l = 0
    node = A
    while node is not None:
        node = node.next
        l += 1
    odd = ((l % 2) == 1)
    l //= 2
    # print(l)
    node = A
    prev = None
    for i in range(l):
        temp = node.next
        node.next = prev
        prev = node
        node = temp
    if odd is True:
        node = node.next
    while node is not None:
        if node.val != prev.val:
            return 0
        node = node.next
        prev = prev.next
    return 1


def lPalin2(self, A):
    if not A or not A.next:
        return 1
    temp = A
    length = 0
    while temp:
        length += 1
        temp = temp.next

    mid = length / 2
    temp = A
    prev = None
    for i in range(mid):
        prev = temp
        temp = temp.next

    prev.next = None

    head1 = A

    cur = temp
    prev = None
    nextptr = None
    while cur:
        nextptr = cur.next
        cur.next = prev
        prev = cur
        cur = nextptr

    head2 = prev

    while head1:
        if head1.val == head2.val:
            head1 = head1.next
            head2 = head2.next
        else:
            return 0
    return 1
