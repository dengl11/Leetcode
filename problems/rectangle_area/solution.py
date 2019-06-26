class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        a1 = (C-A) * (D-B)
        a2 = (G-E) * (H-F)
        if E < A:
            (A,B,C,D), (E,F,G,H) = (E,F,G,H), (A,B,C,D)
        if C <= E or (D <= F or B >= H):
            return a1 + a2
        overlapX = min(C,G) -  max(E, A)
        overlapY = min(D,H) -  max(B, F)
        return a1 + a2 - overlapX * overlapY
        