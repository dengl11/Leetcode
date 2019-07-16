class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s, t = 0, len(nums) - 1
        while s < t:
            curr = nums[s]+nums[t]
            if curr == target: return [s+1,t+1]
            elif curr <target: s += 1
            else: t -=1
        