class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        for i in range(m):
            if A[i][0] == 0:
                A[i] = [1-x for x in A[i]]
        def flipColumn(j):
            for i in range(m):
                A[i][j] = 1- A[i][j]
        
        for j, col in enumerate(zip(*A)):
            if sum(col) < m / 2:
                flipColumn(j)
        ans = 0
        for row in A:
            for j, val in enumerate(row[::-1]):
                ans += val << j
        return ans