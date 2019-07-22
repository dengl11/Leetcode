class Solution:
    def rob(self, nums: List[int]) -> int:
        take, ignore = 0, 0
        
        for x in nums:
            take, ignore = x + ignore, max(take, ignore)
            
        return max(take, ignore)
        