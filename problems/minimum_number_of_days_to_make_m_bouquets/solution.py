from itertools import groupby
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay): return -1
        def ok(d):
            on = [i <= d for i in bloomDay]
            if sum(on) < m * k: return False
            curr = 0
            for state, it in groupby(on):
                if not state: continue
                curr += len(list(it)) // k 
            return curr >= m
        lo, hi = 1, max(bloomDay)
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid): 
                hi = mid
            else:
                lo = mid + 1
        if ok(lo): return lo
        return -1
            