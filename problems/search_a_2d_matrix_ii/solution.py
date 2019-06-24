from bisect import bisect_right
class Solution:
    def searchMatrix(self, M, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not M or not M[0]: return False
        if target < M[0][0] or target > M[-1][-1]: return False
        m, n = len(M), len(M[0])
        start = 0
        for r in M:
            c = bisect_right(r, target) - 1
            if r[c] == target: return True
        return False
            