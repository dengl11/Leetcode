from collections import Counter
class Solution(object):
    def canDivideIntoSubsequences(self, nums, K):
        """
        :type nums: List[int]
        :type K: int
        :rtype: bool
        """
        if len(nums) < K: return False
        c = Counter(nums)
        maxFre = max(c.values())
        return maxFre * K <= len(nums)
        