class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def next(i, j):
            live = 0
            for ni, nj in [(i, j+1), (i, j-1), (i+1, j), (i-1, j), (i+1, j+1), (i+1, j-1), (i-1, j+1), (i-1, j-1)]:
                if ni < 0 or nj < 0 or ni >= m or nj >= n: continue
                if board[ni][nj] & 1:
                    live += 1
            if board[i][j] & 1:
                return live >= 2 and live <= 3
            return live == 3
        
        for i in range(m):
            for j in range(n):
                board[i][j] += int(next(i, j)) << 1
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
                    
                
        