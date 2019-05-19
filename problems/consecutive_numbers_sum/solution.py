class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        ans = 0
        for k in range(1, N+1):
            m = N*2 - (k**2 - k)
            if m <= 0: break
            if m%(2*k) != 0: continue
            ans += 1
        return ans