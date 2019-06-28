class BIT:
    def __init__(self, ma):
        self.data = [0]*(ma+1)
    
    def add(self, x):
        while x < len(self.data):
            self.data[x] += 1
            x += (x & (-x))
    
    def query(self, x):
        ans = 0
        x -= 1
        while x:
            ans += self.data[x]
            x -= (x & (-x))
        return ans
            

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        indexes = {v: i for i,v in enumerate(sorted(set(nums)), 1)}
        ans = []
        bit = BIT(len(indexes) + 1)
        for x in nums[::-1]:
            index = indexes[x]
            ans.append(bit.query(index))
            bit.add(index)
        return ans[::-1]
