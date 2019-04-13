from collections import defaultdict

class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        dp = [[2]*n for _ in range(n)]
        pos = {x:i for (i, x) in enumerate(A)}
        ans = 0
        for k in range(2, n):
            for j in range(k):
                x = A[k] - A[j]
                i = pos.get(x, -1)
                if i >= 0 and i < j:
                    dp[j][k] = dp[i][j] + 1
                    ans = max(ans, dp[j][k])
        return ans
                    