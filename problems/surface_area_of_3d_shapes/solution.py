class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid),len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                h = grid[i][j]
                if h == 0:
                    continue
                ans += 2 # top/bottom
                if i == 0:
                    ans += h
                if i == m - 1:
                    ans += h
                if i > 0:
                    ans += max(0, h - grid[i-1][j])
                if i < m-1:
                    ans += max(0, h - grid[i+1][j])
                if j == 0:
                    ans += h
                if j == n - 1:
                    ans += h
                if j > 0:
                    ans += max(0, h - grid[i][j-1])
                if j < n-1:
                    ans += max(0, h - grid[i][j + 1])
        return ans
                    