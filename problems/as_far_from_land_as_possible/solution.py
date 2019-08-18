from heapq import heappush, heappop
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = []
        dist = dict()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    heappush(q, (0, i, j))
        if not q: return -1
        while q:
            d, i, j = heappop(q)
            if (i, j) in dist: continue
            dist[(i, j)] = d
            for ni, nj in [(i, j + 1), (i + 1, j), (i, j - 1), (i-1, j)]:
                if ni >= m or ni < 0 or nj < 0 or nj >= n: continue
                if (ni, nj) in dist: continue
                heappush(q, (d + 1, ni, nj))
        ans = max(dist.values())
        return ans if ans > 0 else -1