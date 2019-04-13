from math import gcd
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        if q == 0: return 0
        mcm = p * q // gcd(p, q)
        x, y = mcm//q, mcm//p
        if y % 2 == 1:
            return 1 if x % 2 == 1 else 2
        return 0