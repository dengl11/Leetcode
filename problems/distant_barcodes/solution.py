from collections import Counter
from functools import reduce
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        c = Counter(barcodes)
        g = max(c.values())-1
        mosts = [k for k in c if c[k] == g + 1]
        if len(mosts) > 1:
            g += 1
        groups = [[] for _ in range(g)]
        C = None
        curr = 0
        for k, v in sorted(c.items(), key = lambda x:-x[1]):
            if len(mosts) == 1 and C is None: 
                C = k
                v -= 1
            for i in range(v):
                groups[curr].append(k)
                curr = (curr+1) % g
        ans = reduce(lambda x,y: x+y, groups, [])
        if len(mosts) > 1: return ans
        return ans + [C]
