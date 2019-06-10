from heapq import heappop, heappush
class Solution:
    def trapRainWater(self, M: List[List[int]]) -> int:
        if not M or not M[0]: return 0
        q = []
        m, n = len(M), len(M[0])
        visited = set()
        for i in range(m):
            heappush(q, (M[i][0], i, 0))
            heappush(q, (M[i][n-1], i, n-1))
            visited.add((i, 0))
            visited.add((i, n-1))
        
        for j in range(n):
            heappush(q, (M[0][j], 0, j))
            heappush(q, (M[m-1][j], m-1, j))
            visited.add((0, j))
            visited.add((m-1, j))
        
        water = 0
        while q:
            h, i, j = heappop(q)
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ci, cj = i + di, j + dj
                if ci < 0 or ci >= m or cj < 0 or cj >= n: continue
                if (ci, cj) in visited: continue
                # print((i, j), (ci, cj), max(h - M[ci][cj], 0))
                water += max(h - M[ci][cj], 0)
                visited.add((ci, cj))
                heappush(q, (max(h, M[ci][cj]), ci, cj))
        return water