from collections import defaultdict
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = defaultdict(int)
        dp[0] = 0
        for n in rods:
            for k, v in list(dp.items()):
                dp[k+n] = max(dp[k+n], v)
                dp[abs(k-n)] = max(dp[abs(k-n)], min(v+k, v + n))
        return dp[0]
        