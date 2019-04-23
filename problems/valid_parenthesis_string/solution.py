class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0
        for c in s:
            if c == "(":
                hi += 1
                lo += 1
            elif c == ")":
                hi -= 1
                lo -= 1
            else:
                hi += 1
                lo -= 1
            if hi < 0: return False
            if lo < 0: lo = 0
        return hi >= 0 and lo <= 0