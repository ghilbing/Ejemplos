class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node

    def search(self, k):
        p = self.head
        if p != None:
            while p.next != None:
                if (p.data == k):
                    return p
                p = p.next
            if (p.data == k):
                return p
        return None

    def remove(self, p):
        tmp = p.prev
        p.prev.next = p.next
        p.prev = tmp

    def __str__(self):
        s = ""
        p = self.head
        if p != None:
            while p.next != None:
                s += p.data
                p = p.next
            s += p.data
        return s


# example code
a = LinkedList()
b = LinkedList()

a.add('2')
a.add('3')
a.add('4')
a.add('5')
a.add('6')
a.add('7')

b.add('5')
b.add('6')
b.add('7')
b.add('8')
b.add('9')
b.add('10')
b.add('11')
b.add('13')
b.add('14')
b.add('15')
b.add('16')
b.add('17')



print a
print b


def getIntersectionNode(a, b):
    countA = 0
    countB = 0

    headA = a
    headB = b

    while a is not None:
        a = a.next
        countA += 1

    while b is not None:
        b = b.next
        countB += 1

    a = headA
    b = headB

    if countA > countB:
        for i in range(countA - countB):
            a = a.next

    else:
        for i in range(countB - countA):
            b = b.next

    for i in range(min(countA, countB)):
        if a is b:
            return a
        a = a.next
        b = b.next

    return None



print getIntersectionNode(a, b)
