class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None
    def connect_next(self, next_node):
        self.next = next_node
        if next_node is not None:
            next_node.pre = self
        
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head = ListNode(None)
        self.last = None
        self.head.connect_next(self.last)
        self.size = 0
        self.k = k
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.size >= self.k: return False
        old_next = self.head.next
        inserted = ListNode(value)
        self.head.connect_next(inserted)
        inserted.connect_next(old_next)
        if self.last is None:
            self.last = inserted
            
        self.size += 1
        return True
            

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.size >= self.k: return False
        
        if self.last is None:
            return self.insertFront(value)
        else:
            appended = ListNode(value)
            self.last.connect_next(appended)
            self.last = appended
            self.size += 1
            return True


    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.size == 0: return False
        self.size -= 1
        self.head.connect_next(self.head.next.next)
        if self.size == 0:
            self.last = None
        return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.size <= 0: return False
        self.size -= 1
        pre = self.last.pre
        pre.connect_next(None)
        if self.size == 0:
            self.last = None
        else:
            self.last = pre
        return True
        
        
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.size == 0: return -1
        return self.head.next.val
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.size == 0: return -1
        return self.last.val
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size >= self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()