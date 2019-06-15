class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)-1):
            gap = nums[i+1] - nums[i] - 1
            if gap > 0:
                if gap < k: k -= gap
                else:
                    return nums[i] + k
        return nums[-1] + k
                