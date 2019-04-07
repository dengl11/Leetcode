class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        if y4 <= y1 or y3 >= y2: return False
        if x4 <= x1 or x3 >= x2: return False
        return True