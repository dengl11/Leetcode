class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if N >= K + W or K == 0: return 1
        dp = [0] * (N+1) # dp[i]: probability that have i points
        accProb = 1
        dp[0] = 1
        for i in range(1, N + 1):
            dp[i] = accProb / W
            if i < K: accProb += dp[i]
            if i >= W: accProb -= dp[i - W]
        return sum(dp[K:])