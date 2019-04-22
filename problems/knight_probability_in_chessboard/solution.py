class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        cache = {} # {(i, j, k): prob of next being on-board}
        def query(i, j, K):
            if i < 0 or i >= N or j < 0 or j >= N: return 0
            if K == 0: return 1
            if (i, j, K) in cache: return cache[(i, j, K)]
            ans = 0
            for di, dj in [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]:
                ii, jj = i + di, j + dj
                ans += query(ii, jj, K-1)
            ans = ans / 8
            cache[(i, j, K)] = ans
            return ans
        return query(r, c, K)
        
                