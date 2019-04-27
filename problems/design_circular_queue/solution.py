class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.data = [None] * k
        self.size = 0
        self.k = k
        self.head = 0
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.size == self.k: return False
        self.size += 1
        self.tail = (self.tail + 1) % self.k
        self.data[self.tail] = value
        return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.size == 0: return False
        self.size -= 1
        self.head = (1 + self.head) % self.k;
        return True
        
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.size == 0: return -1
        return self.data[self.head]
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.size == 0: return -1
        return self.data[self.tail]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()