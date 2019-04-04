from itertools import combinations
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points = set(tuple(x) for x in points)
        ans = -1
        for (x1, y1), (x2, y2) in combinations(points, 2):
            if (x1, y2) in points and (x2, y1) in points:
                if x1 == x2 or y1 == y2: continue
                curr = abs(x1 - x2) * abs(y1 - y2)
                if ans < 0:
                    ans = curr
                else:
                    ans = min(ans, curr)
        return ans if ans >= 0 else 0
        