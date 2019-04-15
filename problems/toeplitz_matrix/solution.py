class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m-1):
            if len(set(matrix[i+j][j] for j in range(min(m-i, n)))) > 1:
                return False
        for j in range(1, n-1):
            if len(set(matrix[i][j+i] for i in range(min(m, n-j)))) > 1:
                return False
        return True