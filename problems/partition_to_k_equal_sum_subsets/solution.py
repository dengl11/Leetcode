from collections import Counter
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0: return False
        g = s // k
        used = [False] * len(nums)
        def dfs(i, curr, k):
            if k == 1: return True
            if curr > g: return False
            if curr == g: return dfs(0, 0, k-1)
            for j in range(i, len(nums)):
                if used[j]: continue
                used[j] = True
                if dfs(j, curr + nums[j], k): return True
                used[j] = False
            return False
        
        return dfs(0, 0, k)