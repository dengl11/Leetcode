class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        cmin = prices[0]
        left = [0]
        for x in prices[1:]:
            left.append(max(x - cmin, left[-1]))
            cmin = min(cmin, x)
        right = [0]
        cmax = prices[-1]
        for x in prices[-2::-1]:
            right.append(max(cmax - x, right[-1]))
            cmax = max(cmax, x)
        # print(left, right)
        return max(l + r for (l, r) in zip(left, right[::-1]))
        
        