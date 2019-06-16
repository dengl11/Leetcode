from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]: return -1
        q = deque([(0, 0, 1)])
        m, n = len(grid), len(grid[0])
        visited = set([(0, 0)])
        while q:
            i, j, l = q.popleft()
            if (i, j) == (m-1, n-1): return l
            for ni, nj in [(i+1, j),\
                           (i-1, j),\
                           (i, j+1),\
                           (i, j-1),\
                           (i-1, j-1),\
                           (i-1, j+1),\
                           (i+1, j-1),\
                           (i+1, j+1),\
                           ]:
                if ni < 0 or ni >= m or nj < 0 or nj >= n: continue
                if grid[ni][nj]: continue
                if (ni, nj) in visited: continue
                visited.add((ni, nj))
                q.append((ni, nj, l + 1))
        return -1

        
        
        