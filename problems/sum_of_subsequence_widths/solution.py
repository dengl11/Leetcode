from functools import lru_cache
class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        n = len(A)
        ans = 0
        for i, x in enumerate(A):
            ans += x * (1 << i)
            ans -= x * (1 << (n-i-1))
                
        return ans % (10**9 + 7)
        