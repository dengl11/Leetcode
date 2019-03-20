class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    ri, rj = i, j
                    break
        ans = 0
        for x in range(2):
            for i in range(ri + 1, 8):
                if board[i][rj] == 'B': break
                if board[i][rj] == 'p': 
                    ans += 1
                    break
            for i in range(ri - 1, -1, -1):
                if board[i][rj] == 'B': break
                if board[i][rj] == 'p': 
                    ans += 1
                    break
            if x == 0:
                board = list(zip(*board))
                ri, rj = rj, ri
        return ans
                
