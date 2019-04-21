class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        keep, sell = -prices[0], 0
        for i in range(1, len(prices)):
            p = prices[i]
            keep, sell = max(keep, sell - p), max(keep + p - fee, sell) 
        return max(keep, sell)
        