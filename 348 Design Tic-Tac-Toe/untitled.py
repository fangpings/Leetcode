class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.row = [[0, 0] for _ in range(n)]
        self.col = [[0, 0] for _ in range(n)]
        self.diagonal = [[0, 0] for _ in range(2)]

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if row == col:
            self.diagonal[0][player-1] += 1
            print(self.diagonal)
            if self.diagonal[0][player-1] == self.n:
                return player
        if row + col == self.n - 1:
            self.diagonal[1][player-1] += 1
            print(self.diagonal)
            if self.diagonal[1][player-1] == self.n:
                return player
        self.col[col][player-1] += 1
        if self.col[col][player-1] == self.n:
            return player
        self.row[row][player-1] += 1
        if self.row[row][player-1] == self.n:
            return player
        return 0 

if __name__ == '__main__':
    t = TicTacToe(3)
    print(t.move(1,1,2))
    print(t.move(0,2,2))
    print(t.move(2,0,2))

