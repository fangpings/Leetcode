from copy import deepcopy as dp

def solveNQueens(n):
    if n == 1:
        return [['Q']]
    if n == 0:
        return []
    ret = []
    initial_available = [[True for _ in range(n)] for _ in range(n)]
    initial_board = [['.' for _ in range(n)] for _ in range(n)]
    def rec(board, available, i):
        if i == n:
            for i in range(n):
                board[i] = ''.join(board[i])
            ret.append(board)   
            return
        for j in range(n):
            if available[i][j]:
                new_board = dp(board)
                new_available = dp(available)
                new_board[i][j] = 'Q'
                k = i + 1
                while k < n:
                    new_available[k][j] = False
                    m = k - i
                    if j - m >= 0:
                        new_available[k][j-m] = False
                    if j + m < n:
                        new_available[k][j+m] = False
                    k += 1
                rec(new_board, new_available, i + 1)
    rec(initial_board, initial_available, 0)
    return ret

if __name__ == '__main__':
    print(solveNQueens(6))
