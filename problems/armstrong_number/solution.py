class Solution:
    def isArmstrong(self, N: int) -> bool:
        k = len(str(N))
        ans = 0
        _N = N
        while N:
            N, curr = divmod(N, 10)
            ans += curr ** k
        return ans == _N
        