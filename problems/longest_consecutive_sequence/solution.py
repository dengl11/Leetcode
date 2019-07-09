from functools import lru_cache
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        s = set(nums)
        pre = dict()
        ans = 0
        @lru_cache(None)
        def query(x):
            if x-1 not in s: return 1
            return 1 + query(x-1)
        
        return max(query(x) for x in s)