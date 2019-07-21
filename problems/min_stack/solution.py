from collections import Counter
from heapq import heappush, heappop
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None
        

    def push(self, x: int) -> None:
        if self.min is None: 
            self.min = x
            self.stack.append(0)
        else:
            self.stack.append(x - self.min)
            self.min = min(self.min, x)
            

    def pop(self) -> None:
        x = self.stack.pop()
        if x < 0:
            self.min -= x
        if not self.stack:
            self.min = None

    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.min
        else:
            return self.min + self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
