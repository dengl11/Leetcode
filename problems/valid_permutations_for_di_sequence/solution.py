from collections import deque
class Solution(object):
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        mod = 10**9 + 7
        n = len(S)
        dp = deque([1]*(n+1))
        for c in S:
            if c == "I":
                dp.pop()
                for i in range(1, len(dp)):
                    dp[i] += dp[i-1]
            else:
                dp.popleft()
                for i in range(len(dp)-2, -1, -1):
                    dp[i] += dp[i+1]
        return dp[0]%mod
                