from functools import lru_cache
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        neg = n < 0
        n = abs(n)
        
        @lru_cache(None)
        def query(n):
            ans = x
            c = 1
            while n >= 2 * c:
                ans *= ans
                c *= 2
            n -= c
            return ans if n == 0 else ans * query(n)
        
        ans = query(n)
        return 1/ans if neg else ans