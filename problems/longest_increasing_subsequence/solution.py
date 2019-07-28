from bisect import bisect_left as bl
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        L = 0
        for i, x in enumerate(nums):
            j = bl(dp, x, lo=0, hi = max(L, 0))
            if j == L:
                L += 1
            dp[j] = x
        return L