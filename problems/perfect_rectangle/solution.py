from collections import Counter
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        x1 = y1 = float('inf')
        x2 = y2 = 0
        points = Counter()
        for xl, yl, xr, yr in rectangles:
            x1 = min(x1, xl)
            y1 = min(y1, yl)
            x2 = max(x2, xr)
            y2 = max(y2, yr)
            area += (xr - xl) * (yr - yl)
            points[(xl, yl)] += 1
            points[(xr, yr)] += 1
            points[(xl, yr)] += 1
            points[(xr, yl)] += 1
        if area != (x2-x1)*(y2-y1): return False
        if points[(x1, y1)] != 1: return False
        if points[(x2, y2)] != 1: return False
        if points[(x1, y2)] != 1: return False
        if points[(x2, y1)] != 1: return False
        del points[(x1, y1)]
        del points[(x2, y2)]
        del points[(x2, y1)]
        del points[(x1, y2)]
        return all(x%2 == 0 for x in points.values())
        
        