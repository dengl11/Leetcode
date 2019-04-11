class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = []
        visited = [[False]*C for _ in range(R)]
        n = R * C
        i, j = r0, c0
        di = -1
        d = directions[0]
        
        def within(ii, jj):
            return ii >= 0 and ii < R and jj >= 0 and jj < C
            
        
        def get_neighbor(i, j):
            return [(ii, jj) for (ii, jj) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)] if within(ii, jj) ]
        
        cl = 0
        curr = 0
        pre = (0, 0)
        while n:
            if within(i, j):
                visited[i][j] = True
                ans.append([i, j])
                n -= 1
                
            hasNeighbor = any([(ii, jj) != pre and visited[ii][jj] for (ii, jj) in get_neighbor(i, j)])
            
            curr += 1
            if not hasNeighbor:
                di = (di + 1) % 4
                d = directions[di]
            ii, jj = i + d[0], j + d[1]
            pre = (i, j)
            i, j = ii, jj 
            
        return ans
                
            
        