class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2 or k == 0: return 0
        n = len(prices)
        if k >= n//2:
            return sum(max(y - x, 0) for (x, y) in zip(prices, prices[1:]))
        # once = [[0]*n for _ in range(n)]
        # for i in range(n):
        #     cmin = prices[i]
        #     for j in range(i+1, n):
        #         once[i][j] = max(prices[j] - cmin, 0)
        #         cmin = min(cmin, prices[j])
        ans = [0]*n
        for _ in range(k):
            A = ans[:]
            tmp = -prices[0]
            for i in range(1, n):
                A[i] = max(A[i-1],  prices[i] + tmp)
                tmp = max(tmp, ans[i-1] - prices[i])
            ans = A
                    
        return ans[-1]
        