class Solution:
    def updateBoard(self, board, click):
        self.board = board
        self.m = len(board)
        if not self.m:
            return board
        self.n = len(board[0])
        if not self.n:
            return board
        i, j = click
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        else:
            self.reveal(i, j)
            return self.board

    def reveal(self, i, j):
        if i < 0 or i == self.m or j < 0 or j == self.n or self.board[i][j] != 'E':
            return
        count = self.count(i, j)
        if count > 0:
            self.board[i][j] = str(count)
        elif count == 0:
            self.board[i][j] = 'B'
            self.reveal(i-1, j-1)
            self.reveal(i-1, j)
            self.reveal(i-1, j+1)
            self.reveal(i, j-1)
            self.reveal(i, j+1)
            self.reveal(i+1, j-1)
            self.reveal(i+1, j)
            self.reveal(i+1, j+1)

    def count(self, i, j):
        count = 0
        if i > 0:
            if j > 0 and self.board[i-1][j-1] == 'M':
                count += 1
            if self.board[i-1][j] == 'M':
                count += 1
            if j < self.n - 1 and self.board[i-1][j+1] == 'M':
                count += 1
        if j > 0 and self.board[i][j-1] == 'M':
            count += 1
        if j < self.n - 1 and self.board[i][j+1] == 'M':
            count += 1
        if i < self.m - 1:
            if j > 0 and self.board[i+1][j-1] == 'M':
                count += 1
            if self.board[i+1][j] == 'M':
                count += 1
            if j < self.n - 1 and self.board[i+1][j+1] == 'M':
                count += 1
        return count