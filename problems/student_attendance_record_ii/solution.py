from functools import lru_cache
class Solution:
    def checkRecord(self, n: int) -> int:
        P = [0]*(n+1)
        PL = [0]*(n+1)
        P[0] = PL[0] = 1
        P[1] = 1
        PL[1] = 2
        for i in range(2, n + 1):
            P[i] = PL[i-1]
            PL[i] = (P[i] +  P[i-1] + P[i-2])%1000000007
        ans = PL[n]
        for i in range(n):
            ans += PL[i] * PL[n-i-1]
        return ans % 1000000007