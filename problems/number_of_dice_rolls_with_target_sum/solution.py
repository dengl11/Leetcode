from functools import lru_cache
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        @lru_cache(None)
        def query(n, t):
            if t <= 0: return 0
            if n == 1: return 1 if f >= t else 0
            return sum(query(n-1, t-c) for c in range(1, f + 1))
        
        return query(d, target) % (10**9 + 7)