class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        d = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    d[i][j] = d[i-1][j-1] + 1
                else:
                    d[i][j] = max(d[i][j-1], d[i-1][j])
        return d[-1][-1]
                    
                    