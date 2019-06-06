from heapq import heappush, heappop, heapify
class DoubleHeap:
    def __init__(self, data):
        self.minH = []
        self.maxH = []
        for x in data:
            self.insert(x)
    
    def insert(self, x):
        x = float(x)
        if not self.maxH or self.maxH[0] < -x:
            heappush(self.maxH, -x)
        else:
            heappush(self.minH, x)
        # print("insert: ", x)
        # print(self.maxH)
        # print(self.minH)
        self.balance()
    
    def get_median(self):
        # print()
        # print(self.maxH)
        # print(self.minH)
        left, right = len(self.maxH), len(self.minH)
        if left == right: return float(-self.maxH[0] + self.minH[0]) / 2
        return -self.maxH[0]
    
    def balance(self):
        while len(self.maxH) > len(self.minH) + 1:
            heappush(self.minH, -heappop(self.maxH))
        while len(self.maxH) + 1 <= len(self.minH):
            heappush(self.maxH, -heappop(self.minH))
    
    def remove(self, x):
        if x <= self.get_median():
            self.maxH[self.maxH.index(-x)] = self.maxH[-1]
            self.maxH.pop()
            heapify(self.maxH)
        else:
            self.minH[self.minH.index(x)] = self.minH[-1]
            self.minH.pop()
            heapify(self.minH)
        self.balance()
            

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        dh = DoubleHeap(nums[:k-1])
        ans = []
        for i in range(len(nums)-k+1):
            dh.insert(nums[i+k-1])
            ans.append(dh.get_median())
            dh.remove(nums[i])
        return ans
            