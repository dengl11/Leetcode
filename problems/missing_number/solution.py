class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if i == len(nums) or nums[i] == i: continue
            j = nums[i]
            while j < len(nums) and nums[j] != j:
                t = nums[j]
                nums[j] = j
                j = t
        for i in range(len(nums)):
            if nums[i] != i: return i
            
        return len(nums)