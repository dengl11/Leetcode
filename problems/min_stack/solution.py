from collections import Counter
from heapq import heappush, heappop
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = Counter()
        self.stack = []
        self.q = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.nums[x] += 1
        heappush(self.q, x)
        

    def pop(self) -> None:
        x = self.stack.pop()
        self.nums[x] -= 1
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        while self.nums[self.q[0]] == 0:
            heappop(self.q)
        return self.q[0]
