from math import sqrt
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c < 0: return False
        i = 0
        j = int(sqrt(c))
        while i <= j:
            curr = i*i + j *j
            if curr == c: return True
            if curr < c:
                i += 1
            else:
                j -= 1
        return False
                