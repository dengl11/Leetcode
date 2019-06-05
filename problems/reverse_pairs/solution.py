from bisect import bisect_left
class BIT:
    def __init__(self, n):
        self.data = [0]* (n+1)
        
    def query(self, x):
        ans = 0
        while x < len(self.data):
            ans += self.data[x]
            x += (x & -x)
        return ans
    
    def insert(self, x):
        while x > 0:
            self.data[x] += 1
            x -= (x & -x)


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        snums = sorted(nums)
        ans = 0
        bit = BIT(len(nums))
        for x in nums:
            tgt = bisect_left(snums, 2 * x+1) + 1
            ans += bit.query(tgt)
            bit.insert(bisect_left(snums, x) + 1)
        return ans
            