# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def intervalIntersection(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        ans = []
        i = j = 0
        while i < len(A) and j < len(B):
            a, b = A[i], B[j]
            if a.end < b.start:
                i += 1
                continue
            if b.end < a.start:
                j += 1
                continue
            # has intersection
            start = max(a.start, b.start)
            end = min(a.end, b.end)
            ans.append([start, end])
            if a.end >= b.end:
                j += 1
            if a.end <= b.end:
                i += 1
                
        return ans