from functools import lru_cache
class Solution:
    def strangePrinter(self, S: str) -> int:
        s = ""
        for x in S:
            if not s or s[-1] != x: s += x
        if not s: return 0
        n = len(s)
        dp = [[float('inf')]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
            if i+1 <n:
                dp[i][i+1] = 1 if s[i]==s[i+1] else 2
                
        for d in range(2, n):
            for i in range(n-d):
                j = i + d
                for k in range(i,j):
                    t = dp[i][k] + dp[k+1][j]
                    dp[i][j] = min(dp[i][j], t if s[k] != s[j] else t - 1)
        return dp[0][n-1]
                    