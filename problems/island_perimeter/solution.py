class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        stack = []
        def find():
            for i, r in enumerate(grid):
                for j, x in enumerate(r):
                    if x:
                        return (i, j)
        stack.append(find())
        visited = set([stack[-1]])
        ans = 4
        connected = 0
        while stack:
            i, j = stack.pop()
            for ni, nj in [(i, j + 1), (i, j-1), (i+1, j), (i-1, j)]:
                if ni < 0 or ni >= m or nj < 0 or nj >= n or grid[ni][nj] == 0: continue
                if (ni, nj) not in visited:
                    stack.append((ni, nj))
                    ans += 4
                    visited.add((ni, nj))
                connected += 1
        return ans - connected
