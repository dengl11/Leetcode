class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        xs = sorted(set(x for [x1, y1, x2, y2]  in rectangles for x in [x1, x2]))
        xis = {x:i for (i, x) in enumerate(xs)}
        L = []
        for x1, y1, x2, y2 in rectangles:
            L.append((y1, x1, x2, 1))
            L.append((y2, x1, x2, -1))
        L.sort()
        cy = area = xspan = 0
        counts = [0]*len(xis)
        for k, (y, x1, x2, s) in enumerate(L):
            if y != cy:
                area += (y-cy) * xspan
                cy = y
            for i in range(xis[x1], xis[x2]):
                counts[i] += s
            if k < len(L)-1 and y == L[k+1][0]: continue
            xspan = sum((x2-x1) if c else 0 for (x1, x2, c) in zip(xs, xs[1:], counts))
        return area % (10**9+7)