class Solution:
    def minSteps(self, n: int) -> int:
        c = 1
        ans = 0
        p = 0
        while True:
            if c == n: return ans
            if 2 * c <= n and (n - 2 * c) % c == 0:
                p = c
                c *= 2
                ans += 2
            else:
                ans += 1
                c += p
        