class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        def dfs(i, j):
            if grid[i][j] == 0 or visited[i][j]: return 0
            visited[i][j] = True
            ans = 0
            stack = [(i, j)]
            while stack:
                i, j = stack.pop()
                ans += 1
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ii, jj = i + di, j + dj
                    if ii < 0 or ii >= m or jj < 0 or jj >= n or grid[ii][jj] == 0 or visited[ii][jj]: continue
                    stack.append((ii, jj))
                    visited[ii][jj] = True
            return ans
        return max(dfs(i, j) for i in range(m) for j in range(n))
        