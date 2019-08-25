class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return board
        n = len(board[0])
        if n == 0:
            return board
        for i in range(m):
            for j in range(n):
                count = 0
                if i > 0:
                    if j > 0:
                        count += board[i-1][j-1] >= 1
                    count += board[i-1][j] >= 1
                    if j < n - 1:
                        count += board[i-1][j+1] >= 1
                if j > 0:
                    count += board[i][j-1] >= 1
                if j < n - 1:
                    count += board[i][j+1] >= 1
                if i < m - 1:
                    if j > 0:
                        count += board[i+1][j-1] >= 1
                    count += board[i+1][j] >= 1
                    if j < n - 1:
                        count += board[i+1][j+1] >= 1
                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = 2
                else:
                    if count == 3:
                        board[i][j] = -1
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 1
                elif board[i][j] == 2:
                    board[i][j] = 0
        return board

if __name__ == '__main__':
    sol = Solution()
    inp = [
  [1],
  [1],
  [1]
]
    print(sol.gameOfLife(inp))
