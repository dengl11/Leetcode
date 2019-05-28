class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        curr = sum(nums[:k])
        g = [0]*n
        for i in range(n-k+1):
            g[i] = curr
            if i+k < n:
                curr += nums[i+k] - nums[i]
        pre = [0]*n
        for i in range(k+1, n-2*k+1):
            pre[i] = pre[i-1] if g[pre[i-1]] >= g[i-k] else i-k
        after = [n-k]*n
        for i in range(n-2*k, k-1, -1):
            after[i] = after[i+1] if g[after[i+1]] > g[i+k] else i+k
        ans = []
        S = 0
        # print(pre, after)
        for i in range(k, n-2*k+1):
            curr = g[pre[i]] + g[i] + g[after[i]]
            if curr > S:
                S = curr
                ans = [pre[i], i, after[i]]
        return ans