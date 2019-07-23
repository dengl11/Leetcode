class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        base = n * 10
        
        for x in nums:
            old = nums[x%base - 1]
            if old <= n:
                new = (x%base) * base + old
                nums[x%base-1] = new
        ans = []
        for i, x in enumerate(nums):
            if i+1 != x // base:
                ans.append(i + 1)
        return ans