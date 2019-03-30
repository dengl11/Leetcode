from bisect import bisect
from collections import deque

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.data = deque(sorted(nums)[-k:])
        self.k = k
        

    def add(self, val: int) -> int:
        if len(self.data) == self.k and val <= self.data[0]:
            return self.data[0]
        pos = bisect(self.data, val)
        self.data.insert(pos, val)
        if len(self.data) > self.k: 
            self.data.popleft()
        return self.data[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)