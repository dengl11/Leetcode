class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        n = 0
        while Y > X:
            if Y % 2 == 0:
                Y //= 2
                n += 1
            else:
                Y = (Y + 1) // 2
                n += 2
        return n + X-Y
            