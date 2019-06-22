class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        inc = True
        for i in range(len(nums) - 1):
            j = i + 1
            while j < len(nums) and (nums[j] > nums[i]) != inc:
                j += 1
            if j >= len(nums):
                nums[i], nums[i+1] = nums[i+1], nums[i]
            elif j > i + 1:
                nums[i+1], nums[j] = nums[j], nums[i+1]
            inc = not inc