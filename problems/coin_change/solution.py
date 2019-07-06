class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = float('inf')
        dp = [inf] * (amount + 1)
        dp[0] = 0
        for c in coins:
            if c <= amount:
                dp[c] = 1
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c and dp[i-c] != inf:
                    dp[i] = min(dp[i], dp[i-c] + 1)
        return dp[-1] if dp[-1] != inf else -1
        