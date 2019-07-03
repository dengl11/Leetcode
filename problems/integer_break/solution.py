from functools import lru_cache
class Solution:
    def integerBreak(self, n: int) -> int:
        @lru_cache(None)
        def query(i):
            if i == 2: return 1
            ans = i-1
            for j in range(2, (i+1) //2 + 1):
                ans = max(ans, max(query(j), j) * max(i-j, query(i-j)))
            return ans
        
        return query(n)