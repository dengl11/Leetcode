from itertools import combinations
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        x0, y0 = p1
        p2 = (p2[0]-x0, p2[1]-y0)
        p3 = (p3[0]-x0, p3[1]-y0)
        p4 = (p4[0]-x0, p4[1]-y0)
        points = set([p2, p3, p4])
        for p, q in combinations(points, 2):
            if p[0] * q[0] + p[1] * q[1] == 0:
                expected = (p[0] + q[0], p[1] + q[1])
                remain = points - set([p, q])
                if expected not in remain: return False
                r1 = sum(x**2 for x in p)
                r2 = sum(x**2 for x in q)
                return r1 == r2
        return False
        