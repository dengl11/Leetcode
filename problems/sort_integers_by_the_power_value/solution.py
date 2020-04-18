from functools import lru_cache
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # @lru_cache(None)
        def check(x):
            if x == 1: return 0
            if x%2 == 0: return 1 + check(x // 2)
            return 1 + check(3 *x + 1)
        arr = sorted(range(lo, hi+1), key = check)
        return arr[k-1]