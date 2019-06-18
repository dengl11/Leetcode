class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*(len(nums) + 1)
        right = [1]*(len(nums) + 1)
        for i in range(1, len(nums)):
            ans[i+1] = ans[i] * nums[i-1]
        for i in range(len(nums) - 2, -1, -1):
            right[i+1] = right[i+2] * nums[i+1]
            ans[i+1] *= right[i+1]
        return ans[1:]