class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if grid[i][j] == '0': return 0
            grid[i][j] = '0'
            for ni, nj in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue
                if grid[ni][nj] == '0': continue
                dfs(ni, nj)
            return 1
        
        return sum(dfs(i, j) for i in range(m) for j in range(n))