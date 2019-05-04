from functools import lru_cache
class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        @lru_cache(None)
        def query(i, t):
            if t == 0: return 0
            c = i if i else 2
            if t == 1: return c 
            if i >= 40: return float('inf')
            
            n, r = divmod(t, x)
            return min(c * r + query(i+1, n), c * (x-r) + query(i+1, n+1))
        return query(0, target) - 1
            