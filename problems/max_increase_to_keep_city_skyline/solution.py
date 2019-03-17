class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        rowMax, colMax = [0]*m, [0]*n
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                rowMax[i] = max(rowMax[i], v)
                colMax[j] = max(colMax[j], v)
        ans = 0
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                ans += min(rowMax[i], colMax[j]) - v
        return ans
        
        