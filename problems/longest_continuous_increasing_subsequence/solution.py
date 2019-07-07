class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 0 if not nums else 1
        pre = 1
        for x, y in zip(nums, nums[1:]):
            if y > x:
                pre += 1
            else:
                pre = 1
            ans = max(ans, pre)
        return ans
        