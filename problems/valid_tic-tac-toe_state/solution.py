class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        nx = no = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == "X": nx += 1
                elif board[i][j] == "O": no += 1
        if abs(nx - no) > 1 or nx < no: return False
        bad = {"XXX", "OOO"}
        rows = []
        cols = []
        diags = []
        winner = None
        for j in range(3):
            if "".join(board[i][j] for i in range(3)) in bad: 
                if cols: return False
                if winner and winner != board[0][j]: return False
                winner = board[0][j]
                cols.append(i)
            if "".join(board[j][i] for i in range(3)) in bad:
                if rows: return False
                if winner and winner != board[j][0]: return False
                winner = board[j][0]
                rows.append(i)
        if "".join(board[i][i] for i in range(3)) in bad: 
            if winner is None: winner = board[0][0]
            if rows and cols: return False
        if "".join(board[2-i][i] for i in range(3)) in bad: 
            if winner is None: winner = board[0][-1]
            if rows and cols: return False
        if winner == "X":
            return nx > no
        if winner == "O":
            return nx == no
        return True

        