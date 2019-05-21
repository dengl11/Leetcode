class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        inf = float('inf')
        for (i, j) in hits:
            if grid[i][j] == 1:
                grid[i][j] = -1
        
        def nbrs(i, j):
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ci, cj = i + di, j + dj
                if ci < 0 or ci >= m or cj < 0 or cj >= n: continue
                yield ci, cj
        
        def stick(i, j):
            grid[i][j] = inf
            for ni, nj in nbrs(i, j):
                if grid[ni][nj] == 1:
                    stick(ni, nj)
        
        for j in range(n):
            if grid[0][j] == 1: stick(0, j)
        ans = []
        def put_back(i, j, visited):
            grid[i][j] = inf if i == 0 or any(grid[ni][nj] == inf for ni, nj in nbrs(i, j)) else 1
            ans = 1 if grid[i][j] == inf else 0
            for ni, nj in nbrs(i, j):
                if grid[ni][nj] != 1 or (ni, nj) in visited: continue
                visited.add((ni, nj))
                ans += put_back(ni, nj, visited)
            return ans
        for (i, j) in hits[::-1]:
            ans.append(put_back(i, j, set([(i, j)]))-(grid[i][j] == inf) if grid[i][j] == -1 else 0)
        return ans[::-1]
                