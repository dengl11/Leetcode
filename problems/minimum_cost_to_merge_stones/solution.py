from functools import lru_cache
class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        if (n-1) % (K-1) != 0: return -1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + stones[i]
        
        @lru_cache(None)
        def query(i, j):
            if j - i + 1 < K: return 0
            ans = min(query(i, mid) + query(mid+1, j) for mid in range(i, j, K-1))
            if (j-i) % (K-1) == 0:
                ans += prefix[j+1]-prefix[i]
            return ans
    
        return query(0, n-1)