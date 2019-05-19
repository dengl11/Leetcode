class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        blanks = []
        groups = dict() # {(i, j): g}
        g = 0
        def dfs(i, j, visited):
            visited.add((i, j))
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ci, cj = i + di, j + dj
                if ci >= m or ci < 0 or cj < 0 or cj >= n: continue
                if grid[ci][cj] != 1 or (ci, cj) in visited: continue
                dfs(ci, cj, visited)
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: blanks.append((i, j))
                elif grid[i][j] == 1:
                    g += 1
                    visited = set()
                    dfs(i, j, visited)
                    for ci, cj in visited:
                        grid[ci][cj] = -len(visited)
                        groups[(ci, cj)] = g
                    ans = max(ans, len(visited))
        for i, j in blanks:
            nbrs = []
            used = set() 
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ci, cj = i + di, j + dj
                if ci >= m or ci < 0 or cj < 0 or cj >= n or grid[ci][cj] == 0: continue
                if groups[(ci, cj)] in used: continue
                used.add(groups[(ci, cj)])
                nbrs.append(-grid[ci][cj])
            ans = max(ans, 1 + sum(nbrs))
        return ans
            
                
        