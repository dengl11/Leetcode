class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if not A or not B: return not B and not A
        if len(A) != len(B): return False
        return A in B * 2