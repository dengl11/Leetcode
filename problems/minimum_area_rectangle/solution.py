from itertools import combinations
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points = set(tuple(x) for x in points)
        inf = float('inf')
        ans = inf
        for p1, p2 in combinations(points, 2):
            if p1[0] == p2[0] or p1[1] == p2[1]: continue
            x1, y1 = p1
            x2, y2 = p2
            if (x1, y2) not in points or (x2, y1) not in points: continue
            ans = min(ans, abs(x2 - x1) * abs(y2 - y1))
        return ans if ans != inf else 0
        