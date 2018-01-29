# Definition for singly-linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        node.next=self.head
        self.head = node

    def printl(self):
        current = self.head
        while current:
            print current.data
            current= current.next


    def removeDups(self):
        current = second = self.head
        while current is not None:
            while second.next is not None:  # check second.next here rather than second
                if second.next.data == current.data:  # check second.next.data, not second.data
                    second.next = second.next.next  # cut second.next out of the list
                else:
                    second = second.next  # put this line in an else, to avoid skipping items
            current = second = current.next

    def removeDupsHashTable(self):
        length = 0
        l = self.head
        while(l):
            length +=1
            l = l.next
            if l == None:
                break
        table = []
        for i in list(range(length)):
            table.append([i])
        l = self.head
        while(l):
            key = l.data % length
            if table[key] != l.data:
                table[key] = l.data
                prev = l
                l = l.next
            else:
                prev.next = l.next
                l = l.next
            #print (table)
        print (table)




l= LinkedList()
l.insert(15)
l.insert(14)
l.insert(16)
l.insert(15)
l.insert(15)
l.insert(14)
l.insert(18)
l.insert(159)
l.insert(13)
l.insert(10)
l.insert(15)
l.insert(14)

l.printl()
print "==============="

l.removeDups()

l.printl()


print "==============="
l.removeDupsHashTable()