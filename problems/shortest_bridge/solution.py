from collections import deque
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        def color(i, j):
            stack = [(i, j)]
            while stack:
                i, j = stack.pop()
                A[i][j] = 2
                for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    ci, cj = i + di, j + dj
                    if ci < 0 or cj < 0 or ci >= m or cj >= n: continue
                    if A[ci][cj] != 1: continue
                    stack.append((ci, cj))
        def find1():
            for i in range(m):
                for j in range(n):
                    if A[i][j] == 1:
                        return (i, j)
        color(*find1())
        q = deque()
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    q.append((i, j, 0))
                    A[i][j] = 3
        
        while q:
            i, j, c = q.popleft()
            
            for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                ci, cj = i + di, j + dj
                if ci < 0 or cj < 0 or ci >= m or cj >= n: continue
                if A[ci][cj] == 3: continue
                if A[ci][cj] == 2: return c
                A[ci][cj] = 3
                q.append((ci, cj, c + 1))

        
                    
            
        