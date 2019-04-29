class Solution:
    def findPaths(self, MM: int, NN: int, N: int, i: int, j: int) -> int:
        cache = {} # {(i, j, n): val}
        def query(i, j, n):
            if i < 0 or i >= MM or j < 0 or j >= NN: return 1
            if n == 0: return 0
            if (i, j, n) in cache: return cache[(i, j, n)]
            ans = 0
            for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                ci, cj = i + di, j + dj
                ans += query(ci, cj, n-1)
            cache[(i, j, n)] = ans
            return ans
        return query(i, j, N) % (10**9 + 7)
            