# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = None

    def add(self, data):
        node = ListNode(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node

    def Print(self):
        temp = self.head
        while temp is not None:
            print(temp.val)
            temp = temp.next


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next and p.next.next:
            tmp = p.next.next
            p.next.next = tmp.next
            tmp.next = p.next
            p.next = tmp
            p = p.next.next

    def Print(self, head):
        tmp = head
        while tmp is not None:
            print(tmp.val)
            tmp = tmp.next


if __name__ == '__main__':
    list = LinkedList(None)
    for i in range(1, 11):
        list.add(i)
    list.Print();
    swap = Solution()
    swap.swapPairs(list.head);
    swap.Print(list.head);
