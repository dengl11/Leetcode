from functools import lru_cache
class Solution:
    def longestDecomposition(self, text: str) -> int:
        @lru_cache(None)
        def query(i, j):
            if i > j: return 0
            if i == j: return 1
            ans = 1
            for k in range(1, (j-i + 1)//2 + 1):
                if text[i:i+k] == text[j-k+1:j+1]:
                    ans = max(ans, 2 + query(i+k, j-k))
            return ans
        
        return query(0, len(text) - 1)