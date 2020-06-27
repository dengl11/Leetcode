from functools import lru_cache
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        dp = [[float('inf')] *  (n+1) for _ in range(k+1)]

        @lru_cache(None)
        def min_total(box, pre, j):
            return sum(abs(houses[x-1] - box) for x in range(pre + 1, j+1))
        
        # dp[i][j]: min-distance to have i groups for the first j houses
        for i in range(k+1):
            for j in range(i+1):
                dp[i][j] = 0
        for i in range(1, k+1):
            for j in range(i+1, n+1):
                 for pre in range(j):
                    # [1, ... pre], [pre + 1,..  j]
                    first = dp[i-1][pre]
                    box = houses[(pre + j - 1) // 2]
                    second = min_total(box, pre, j)
                    curr = first + second
                    dp[i][j] = min(dp[i][j], curr)
        return dp[-1][-1]
                    
        