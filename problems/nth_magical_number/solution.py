class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        def gcd(x, y):
            while x:
                y, x = x, y%x
            return y
        if B < A: A, B = B, A
        G = gcd(A, B)
        L = A * B / G
        left, right = 2, N * A
        while left < right:
            mid = (left + right) / 2
            curr = mid/A + mid/B - mid/L
            if curr < N:
                left = mid + 1
            else :
                right = mid
        return left % (10**9+7)