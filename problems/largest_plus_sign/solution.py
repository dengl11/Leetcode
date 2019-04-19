class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        mines = set(tuple(x) for x in mines)
        lefts = [[0]*N for _ in range(N)]
        rights = [[0]*N for _ in range(N)]
        ups = [[0]*N for _ in range(N)]
        downs = [[0]*N for _ in range(N)]
        
        for i in range(N):
            left = 0
            for j in range(N):
                if (i, j) in mines: 
                    left = 0
                else:
                    lefts[i][j] = left
                    left += 1
        for i in range(N):
            right = 0
            for j in range(N-1, -1, -1):
                if (i, j) in mines: 
                    right = 0
                else:
                    rights[i][j] = right
                    right += 1
        for j in range(N):
            up = 0
            for i in range(N):
                if (i, j) in mines: 
                    up = 0
                else:
                    ups[i][j] = up
                    up += 1
        for j in range(N):
            down = 0
            for i in range(N-1, -1, -1):
                if (i, j) in mines: 
                    down = 0
                else:
                    downs[i][j] = down
                    down += 1
        ans = 0
        for i in range(N):
            for j in range(N):
                if (i,j) in mines: continue
                ans = max(ans, 1 + min(lefts[i][j], rights[i][j], ups[i][j], downs[i][j]))
        return ans
                
        