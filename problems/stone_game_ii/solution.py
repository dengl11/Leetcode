from functools import lru_cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        @lru_cache(None)
        def query(i, M):
            if i + 2 * M >= n: return sum(piles[i:])
            ans = -float('inf')
            for j in range(i + 1, i + 2 * M + 1):
                ans = max(ans, sum(piles[i:j]) - query(j, max(M, j - i)))
            return ans
        total = sum(piles)
        return (total + query(0, 1)) // 2