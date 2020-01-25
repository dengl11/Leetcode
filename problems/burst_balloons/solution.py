class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [x for x in nums if x > 0]  + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for k in range(2, n):
            for left in range(0, n-k):
                right = left + k
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], nums[i] * nums[left] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][n-1]
        