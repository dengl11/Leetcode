class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        a, i = max((x, i) for (i, x) in enumerate(nums))
        for j in range(len(nums)):
            if j == i: continue
            if a < nums[j] * 2: return -1
        return i
        
        