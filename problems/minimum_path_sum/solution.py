from functools import lru_cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @lru_cache(None)
        def query(i, j):
            if i < 0 or i >= m or j < 0 or j >= n: return float('inf')
            if (i, j) == (m-1, n-1): return grid[i][j]
            return min(query(i+1, j), query(i, j+1)) + grid[i][j]
        return query(0, 0)