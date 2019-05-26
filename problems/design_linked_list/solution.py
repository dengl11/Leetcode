class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dummy = Node(None)
        self.tail = None
        self.n = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.n: return -1
        curr = self.dummy.next
        while index:
            curr = curr.next
            index -= 1
        return curr.val

    def add_after(self, pre, val):
        tmp = pre.next
        pre.next = Node(val)
        pre.next.next = tmp
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.add_after(self.dummy, val)
        if self.n == 0:
            self.tail = self.dummy.next
        self.n += 1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.n == 0:
            self.addAtHead(val)
        else:
            self.n += 1
            # print(self.n, self.tail, val)
            self.add_after(self.tail, val)
            self.tail = self.tail.next
            # print("addAtTail:", self.n)
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.n: return
        if index < 0:
            index = max(0, self.n + index)
        if index == 0:
            self.addAtHead(val)
        elif index == self.n:
            self.addAtTail(val)
        else:
            self.n += 1
            pre = self.dummy
            while index:
                pre = pre.next
                index -= 1
            # print(pre, val)
            self.add_after(pre, val)
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.n: return
        pre = self.dummy
        while index:
            pre = pre.next
            index -= 1
        if pre.next == self.tail:
            self.tail = pre
        pre.next = pre.next.next
        self.n -= 1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)