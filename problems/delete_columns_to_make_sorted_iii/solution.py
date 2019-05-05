class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        N, n = len(A), len(A[0])
        dp = [1] * n # dp[i]: max length if we keep the i^th column
        for j in range(1, n):
            candidates = [k for k in range(j) if all(A[i][k] <= A[i][j] for i in range(N))]
            curr = max([dp[x] for x in candidates], default = 0)
            dp[j] = curr + 1
        return n - max(dp)
            
            