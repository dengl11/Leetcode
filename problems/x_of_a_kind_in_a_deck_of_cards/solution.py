from collections import Counter
from math import gcd
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        c = Counter(deck)
        size = -1
        for v in c.values():
            if v < 2: return False
            if size < 0: size = v
            else:
                size = gcd(v, size)
        
        return size > 1