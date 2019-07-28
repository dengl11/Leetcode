from collections import Counter
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        if all(x == 0 for r in grid for x in r): return 0
        m, n = len(grid), len(grid[0])
        ans = 1
        right = Counter()
        down = Counter()
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 0: continue
                right[(i, j)] = 1
                down[(i, j)] = 1
                
                if j + 1 < n and right[(i,j+1)]: right[(i,j)] = right[(i,j+1)] + 1
                if i + 1 < m and down[(i+1, j)]: down[(i, j)] = down[(i+1, j)] + 1
        for i in range(m):
            for j in range(n):
                for d in range(1, min(m-i, n - j)):
                    i2 = i + d
                    j2 = j + d
                    if grid[i2][j2] != 1: continue
                    d += 1
                    if right[(i, j)] >= d and right[(i2, j)] >= d and down[(i, j2)] >= d and down[(i, j)] >= d:
                        ans = max(ans, d ** 2)
        return ans
                        