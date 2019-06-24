class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.b = [[0]*n for _ in range(n)]
        self.n = n
        

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.b[row][col] = player
        if all(self.b[row][j] == player for j in range(self.n)):
            return player
        if all(self.b[i][col] == player for i in range(self.n)):
            return player
        if row == col and all(self.b[i][i] == player for i in range(self.n)):
            return player
        if row + col == self.n - 1 and all(self.b[i][self.n -1 - i] == player for i in range(self.n)):
            return player
        return 0