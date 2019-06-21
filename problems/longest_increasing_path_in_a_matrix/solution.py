from functools import lru_cache
from itertools import product
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        
        @lru_cache(None)
        def query(i, j):
            x = matrix[i][j]
            return 1 + max([query(ni, nj) for (ni, nj) in \
                           [(i, j+1), (i, j-1), (i+1, j), (i-1, j)] \
                           if ni >= 0 and ni < m and nj >= 0 and nj < n and matrix[ni][nj] > x], \
                           default = 0)
    
        return max(query(i, j) for (i, j) in product(range(m), range(n)))