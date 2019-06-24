class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        ans = nums[0]
        curr = ans
        for x in nums[1:]:
            curr = max(curr + x, x)
            ans = max(ans, curr)
        return ans
        