class Solution(object):
    def numberOfDays(self, Y, M):
        """
        :type Y: int
        :type M: int
        :rtype: int
        """
        if M != 2: return [0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][M]
        def leap(y):
            if y % 4: return False
            if y % 100 == 0:
                if y % 400 == 0: return True
                return False
            return True
        if leap(Y): return 29
        return 28
        