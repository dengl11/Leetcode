from collections import Counter
from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort(reverse=True)
        c = Counter(nums)
        s = sum(nums)
        if s%2: return False
        tgt = s // 2
        pairs = list(c.items())
        @lru_cache(None)
        def dfs(i, curr = 0):
            if curr == tgt: return True
            if i >= len(pairs) or curr > tgt: return False
            for k in range(pairs[i][1], -1, -1):
                if dfs(i + 1, curr + pairs[i][0] * k):
                    return True
            return False
        return dfs(0)
