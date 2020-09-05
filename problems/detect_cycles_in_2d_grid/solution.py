class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = set()
        def dfs(i, j, dist, curr):
            if (i, j) in dist: # cycle detected
                L = curr - dist[(i, j)]
                if L >= 4: return True
                return False
            dist[(i, j)] = curr
            for ni, nj in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if ni >= m or nj >= n or ni < 0 or nj < 0 or grid[i][j] != grid[ni][nj]: continue
                if (ni, nj) not in visited:
                    if dfs(ni, nj, dist, curr + 1):
                        return True
            visited.add((i, j))
            return False
        for i in range(m):
            for j in range(n):
                if (i, j) in visited: continue
                if dfs(i, j, {}, 1):
                    return True
        return False