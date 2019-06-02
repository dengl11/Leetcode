class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        points.sort()
        def cross(O, A, B):
            O, A, B = points[O], points[A], points[B]
            v1x, v1y = A[0]-O[0], A[1]-O[1]
            v2x, v2y = B[0]-O[0], B[1]-O[1]
            return v1x * v2y - v2x * v1y
        # lower part
        lower = []
        for p in range(len(points)):
            while len(lower) > 1 and cross(lower[-2], p, lower[-1]) > 0:
                lower.pop()
            lower.append(p)
        # upper part
        upper = []
        for p in range(len(points)-1, -1, -1):
            while len(upper) > 1 and cross(upper[-2], p, upper[-1]) > 0:
                upper.pop()
            upper.append(p)
        
        return [points[i] for i in set(lower + upper)]