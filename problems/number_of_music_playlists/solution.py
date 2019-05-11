from functools import lru_cache
class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        def helper(n):
            ans = 1
            for i in range(K):
                ans *= (n-i)
            for _ in range(L-K):
                ans *= (n-K)
            return ans
        def C(n, i):
            ans = n
            for k in range(1, i):
                ans *= (n-k)
            while i:
                ans //= i
                i -= 1
            return ans
        @lru_cache(None)
        def query(N):
            if N <= K: return 0
            ans = helper(N)
            for i in range(1, N-K):
                ans -= C(N, i) * query(N-i)
            return ans % (10**9+7)
        return query(N)