class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j] != 5: continue
                if grid[i-1][j] + grid[i+1][j] != 10: continue
                if grid[i][j-1] + grid[i][j+1] != 10: continue
                if grid[i-1][j-1] + grid[i+1][j+1] != 10: continue
                if grid[i-1][j+1] + grid[i+1][j-1] != 10: continue
                if grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] != 15: continue
                if grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1] != 15: continue
                if grid[i-1][j-1] + grid[i][j-1] + grid[i+1][j-1] != 15: continue
                if grid[i-1][j+1] + grid[i][j+1] + grid[i+1][j+1] != 15: continue
                if len(set(grid[i-1][j-1:j+2] + grid[i][j-1:j+2] + grid[i+1][j-1:j+2])) != 9:
                    continue
                if max(grid[i-1][j-1:j+2] + grid[i][j-1:j+2] + grid[i+1][j-1:j+2]) > 9:
                    continue
                if min(grid[i-1][j-1:j+2] + grid[i][j-1:j+2] + grid[i+1][j-1:j+2]) < 1:
                    continue
                ans += 1
        return ans