from heapq import heappop, heappush
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False]*n for _ in range(n)]
        visited[0][0] = True
        ans = grid[0][0]
        q = [(ans, 0, 0)]
        while q:
            T, i, j = heappop(q)
            ans = max(ans, T)
            if i == j == n-1: return ans
            for ni, nj in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
                if ni < 0 or ni >= n or nj < 0 or nj >= n: continue
                if visited[ni][nj]: continue
                visited[ni][nj] = True
                heappush(q, (grid[ni][nj], ni, nj))
        
            