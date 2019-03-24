from itertools import permutations
from math import gcd, sqrt
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        points = [tuple(x) for x in points]
        pointsSet = set(points)
        def dist(p1, p2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return sqrt(dx ** 2 + dy ** 2)
        inf = float('inf')
        ans = inf
        for p1, p2, p3 in permutations(points, 3):
            dx1, dy1 = p2[0] - p1[0], p2[1] - p1[1]
            dx2, dy2 = p3[0] - p1[0], p3[1] - p1[1]
            if dx1 *dx2 + dy1 * dy2 != 0: continue
            p4x = p3[0] + dx1
            p4y = p3[1] + dy1
            p4 = (p4x, p4y)
            if p4 not in pointsSet: continue
            l1, l2 = dist(p1, p2), dist(p1, p3)
            ans = min(ans, l1 * l2)
        return ans if ans != inf else 0
