class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for curr, n in zip(prices, prices[1:]):
            if curr < n:
                ans += n - curr
        return ans
        