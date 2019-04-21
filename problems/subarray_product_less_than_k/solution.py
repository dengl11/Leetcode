class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k < 0: return 0
        pre = 0
        curr = 1
        ans = 0
        for i, x in enumerate(nums):
            curr *= x
            while pre <= i and curr >= k:
                curr //= nums[pre]
                pre += 1
            ans += i-pre + 1
        return ans
        