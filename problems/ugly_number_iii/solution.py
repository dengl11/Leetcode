from math import gcd
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        if 1 in [a, b, c]: return n
        
        lc = lambda x, y: x * y // gcd(x, y)
        ab, ac, bc = lc(a, b), lc(a, c), lc(b, c)
        abc = lc(ab, c)
        lo = min(a, b, c)
        hi = 2 * (10 ** 9)
        
        def count(x):
            return (x // a) + (x // b) + (x // c) - (x // ab) - (x// bc) - (x//ac) + (x //abc)
        
        while lo < hi:
            mi = (lo + hi) // 2
            if count(mi) < n:
                lo = mi + 1
            else:
                hi = mi
        return lo
            