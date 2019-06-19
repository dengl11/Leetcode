class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        if not prices: return 0
        lowest = prices[0]
        for x in prices:
            ans = max(ans, x - lowest)
            lowest = min(lowest, x)
        return ans
        