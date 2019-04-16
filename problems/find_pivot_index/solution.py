class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        accSum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            accSum[i] = accSum[i-1] + nums[i-1]
        for i in range(1, len(nums) + 1):
            left = accSum[i-1]
            right = accSum[-1] - accSum[i]
            if left == right:
                return i-1
        return -1