class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int: 
        start = None
        todo = 2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: start = (i, j)
                if grid[i][j] == 0: todo += 1
        def dfs(i, j, visited):
            if grid[i][j] == 2: return 1 if len(visited) == todo else 0
            ans = 0
            for di, dj in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                ci, cj = i + di, j + dj
                if ci < 0 or ci >= len(grid) or cj < 0 or cj >= len(grid[0]): continue
                if (ci, cj) in visited or grid[ci][cj] < 0: continue
                visited.add((ci, cj))
                ans += dfs(ci, cj, visited)
                visited.remove((ci, cj))
            return ans
            
        return dfs(*start, set([start]))
        