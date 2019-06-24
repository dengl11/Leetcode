class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0: return 0
        neg = (dividend < 0) != (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend < divisor: return 0
        ans = 1
        curr = divisor
        while curr + curr <= dividend:
            ans <<= 1
            curr <<= 1
        ans += self.divide(dividend - curr, divisor)
        ans = ans if not neg else -ans
        if ans > (1 << 31) - 1: return (1 << 31) - 1
        if ans < -(1 << 31): return - (1<<31)
        return ans