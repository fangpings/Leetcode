from collections import defaultdict

def isValidSudoku(board):
    row = [defaultdict(int) for _ in range(9)]
    column = [defaultdict(int) for _ in range(9)]
    box = [defaultdict(int) for _ in range(9)]
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == '.':
                continue
            row[i][num] += 1
            if row[i][num] > 1:
                return False
            column[j][num] += 1
            if column[j][num] > 1:
                return False
            box[(i//3)*3+j//3][num] += 1
            if box[(i//3)*3+j//3][num] > 1:
                return False
    return True

if __name__ == '__main__':
    a = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    print(isValidSudoku(a))

