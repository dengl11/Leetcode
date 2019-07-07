from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        inf = float('inf')
        m, n = len(grid), len(grid[0])
        total = [[0]*n for _ in range(m)]
        empty = 0
        for I in range(m):
            for J in range(n):
                if grid[I][J] != 1: continue
                # for r in grid:
                #     print(r)
                # for c in total:
                #     print(c)
                miDist = inf
                q = deque([(I, J, 0)])
                # dist = [[float('inf')]*n for _ in range(m)]
                while q:
                    i, j, c = q.popleft()
                    for ni, nj in [(i, j + 1), (i, j - 1), (i+1, j), (i-1, j)]:
                        if ni < 0 or ni >= m or nj < 0 or nj >= n: continue
                        if grid[ni][nj] != empty: continue
                        # print("update:", ni, nj)
                        # dist[ni][nj] = c + 1
                        grid[ni][nj] -= 1
                        total[ni][nj] += c + 1
                        miDist = min(miDist, total[ni][nj])
                        q.append((ni, nj, c + 1))
                empty -= 1
        return miDist if miDist != inf else -1
                        
                
                