class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])
        while 1:
            changed = False
            for i in range(m):
                for j in range(n-2):
                    if board[i][j] != 0 and abs(board[i][j]) == abs(board[i][j+1]) == abs(board[i][j+2]):
                        changed = True
                        board[i][j] = board[i][j+1] = board[i][j+2] = -abs(board[i][j])
                                                          
            for i in range(m-2):
                for j in range(n):
                    if board[i][j] != 0 and abs(board[i][j]) == abs(board[i+1][j]) == abs(board[i+2][j]):
                        changed = True
                        board[i][j] = board[i+1][j] = board[i+2][j] = -abs(board[i][j])
            if not changed:
                  return board
            
            for j in range(n):
                wr = m-1
                for i in range(m-1, -1, -1):
                    if board[i][j] > 0:
                        board[wr][j] = board[i][j]
                        wr -= 1
                for i in range(wr+1):
                    board[i][j] = 0
            
                
                    
            
                                                          
