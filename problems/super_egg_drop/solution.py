class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [0]*(K+1)
        m = 0
        while dp[-1] < N:
            for i in range(K, 0, -1):
                dp[i] += 1 + dp[i-1]
            m += 1
        return m