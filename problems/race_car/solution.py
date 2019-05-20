from functools import lru_cache
class Solution:
    def racecar(self, target: int) -> int:
        @lru_cache(None)
        def query(i):
            if i <= 1: return i
            n = i.bit_length()
            if (1<<n) - 1 == i: return n
            ans = n + query((1<<n) -1 - i) + 1
            for m in range(n-1):
                ans = min(ans, query(i + (1<<m) - (1<<(n-1))) + m + n + 1)
            return ans
        
        return query(target)
                
        