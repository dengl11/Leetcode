class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            self.M = None
            return
        m, n = len(matrix),len(matrix[0])
        self.M = [[0]*n for _ in range(m)]  
        for r in range(m):
            self.M[r][0] = (self.M[r-1][0] if r > 0 else 0) + matrix[r][0]
            for c in range(1, n):
                self.M[r][c] = self.M[r][c-1] + (self.M[r-1][c] if r > 0 else 0) + matrix[r][c] - ( self.M[r-1][c-1] if r > 0 else 0)
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.M is None: return 0
        x = self.M[row2][col1-1] if col1 > 0 else 0
        y = self.M[row1-1][col2] if row1 > 0 else 0
        z = self.M[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        return self.M[row2][col2] - x - y + z
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)