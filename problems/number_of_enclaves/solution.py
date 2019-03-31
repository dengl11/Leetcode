class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        visited = [[False] * n for _ in range(m)]
        def explore(i, j):
            if visited[i][j] or A[i][j] == 0: return
            visited[i][j] = True
            stack = [(i, j)]
            while stack:
                i,j  = stack.pop()
                A[i][j] = 0
                for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    ii, jj = i + di, j + dj
                    if ii < 0 or jj < 0 or ii >= m or jj >= n or A[ii][jj] == 0 or visited[ii][jj]:
                        continue
                    visited[ii][jj] = True
                    stack.append((ii, jj))
        for i in range(m):
            explore(i, 0)
            explore(i, n - 1)
        for j in range(n):
            explore(0, j)
            explore(m - 1, j)
        return sum(sum(row) for row in A)
        
                
            
            