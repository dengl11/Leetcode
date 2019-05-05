from math import gcd
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        def k(p1, p2):
            dx,dy = p2[0]-p1[0], p2[1]-p1[1]
            if dx < 0: dx, dy = -dx, -dy
            g = gcd(dx, dy)
            return (dx//g, dy//g)
        return len(set(tuple(x) for x in points)) == 3 and k(points[0], points[1]) != k(points[0], points[2])