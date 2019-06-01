from functools import lru_cache
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [0]*(k+1)
        dp[0] = 1
        if k == 0: return 1
        if n >= 2:
            dp[1] = 1
        for I in range(3, n+1):
            curr = [0]*(k+1)
            curr[0] = 1
            for m in range(1, k+1):
                curr[m] += curr[m-1] + dp[m]
                if m >= I:
                    curr[m] -= dp[m-I]
            # for j in range(1, min(I, k+1)):
            #     for m in range(j, k+1):
            #         curr[m] += dp[m-j]
            #         print(j, m)
            # print(curr)
            # print(curr)
            dp = curr
            # print(I)
            # print(dp)
        return dp[-1] % (10**9+7)