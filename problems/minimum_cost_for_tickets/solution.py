class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        inf = float('inf')
        dp = [inf for _ in range(n)]
        for i, today in enumerate(days):
            pre = dp[i-1] if i > 0 else 0
            # 1) buy a one-day ticket today
            dp[i] = min(dp[i], pre + costs[0])
            # 1) buy a 7-day ticket today
            j = i
            while j < n and days[j] - today < 7:
                dp[j] = min(dp[j], pre + costs[1])
                j += 1
            # 2) buy a 30-day ticket today
            j = i
            while j < n and days[j] - today < 30:
                dp[j] = min(dp[j], pre + costs[2])
                j += 1
        return dp[-1]
        