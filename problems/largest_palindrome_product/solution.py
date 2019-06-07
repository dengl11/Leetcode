from math import sqrt
class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1: return 9
        for a in range(2, 9*10**n):
            H = 10**n - a
            L = int(str(H)[::-1])
            C = a ** 2 - 4 * L
            if C < 0: continue
            i = sqrt(C)
            if int(i) != i: continue
            i = int(i)
            if (i + a) % 2 != 0: continue
            ans = 10 ** n * (10 ** n - a) + L
            return ans % 1337
        