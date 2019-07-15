from itertools import accumulate               
from bisect import bisect
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        acc = [0] + list(accumulate([2*(h>8) -1 for h in hours]))
        def ok(k):
            mi = 0
            for i in range(k, len(acc)):
                mi = min(mi, acc[i-k])
                if acc[i] > mi: return True
            return False
        
        lo, hi = 0, len(hours)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
        