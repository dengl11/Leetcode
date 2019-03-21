from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        nFresh = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append(((i, j), 0))
                elif grid[i][j] == 1:
                    nFresh += 1
        
        t = 0
        while q:
            (i, j), t = q.popleft()
            for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                ii, jj = i + di, j + dj
                if ii >= 0 and ii < m and jj < n and jj >= 0:
                    if grid[ii][jj] == 1:
                        grid[ii][jj] = 2
                        nFresh -= 1
                        q.append(((ii, jj), t+1))
        return t if nFresh == 0 else -1