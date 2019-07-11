class Solution:
    def solve(self, board):
        self.m = len(board)
        if self.m == 0:
            return
        self.n = len(board[0])
        if self.n == 0:
            return
        self.label = [[0 for _ in range(self.n)] for _ in range(self.m)]
        board = board
        def find(i, j):
            if self.label[i][j]:
                return
            self.label[i][j] = 1
            if i > 0 and board[i-1][j] == 'O':
                find(i-1, j)
            if j > 0 and board[i][j-1] == 'O':
                find(i, j-1)
            if i < self.m - 1 and board[i+1][j] == 'O':
                find(i+1, j)
            if j < self.n - 1 and board[i][j+1] == 'O':
                find(i, j+1)
        for i in range(self.m):
            if board[i][0] == 'O':
                find(i, 0)
            if board[i][self.n-1] == 'O':
                find(i, self.n-1)
        for j in range(self.n):
            if board[0][j] == 'O':
                find(0, j)
            if board[self.m-1][j] == 'O':
                find(self.m-1, j)
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == 'O' and self.label[i][j] == 0:
                    board[i][j] = 'X'

if __name__ == '__main__':
    sol = Solution()
    board = 



