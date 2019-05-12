class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        dp = [0] * (n+K)
        for i in range(n):
            currMax = 0
            for k in range(1, min(K+1, i+2)):
                currMax = max(currMax, A[i-k+1])
                dp[i] = max(dp[i], dp[i-k] + currMax * k)
        return dp[n-1]
                
            