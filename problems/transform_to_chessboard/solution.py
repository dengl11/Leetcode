class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        if any(board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j] for i in range(n) for j in range(n)):
            return -1
        if not (n//2 <= sum(board[0][j] for j in range(n)) <= (n+1)//2): return -1
        if not (n//2 <= sum(board[i][0] for i in range(n)) <= (n+1)//2): return -1
        c = sum(board[0][j] != j%2 for j in range(n))
        r = sum(board[i][0] != i%2 for i in range(n))
        if n % 2:
            if c % 2: c = n - c
            if r % 2: r = n - r
        else:
            c = min(c, n-c)
            r = min(r, n-r)
        return (r + c) //2
        