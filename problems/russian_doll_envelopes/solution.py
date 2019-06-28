from bisect import bisect_left as bl
class Solution(object):
    def maxEnvelopes(self, env):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def lis(arr):
            dp = [0] * len(arr)
            L = 0
            for x in arr:
                i = bl(dp, x, lo = 0, hi = max(L, 0))
                if i == L:
                    L += 1
                dp[i] = x
            return L
        env.sort(key = lambda x: (x[0], -x[1]))
        return lis([x[1] for x in env])
