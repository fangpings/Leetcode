class Solution:
    def exist(self, board, word):
        row, col = len(board), len(board[0])
        if len(word) == 1:
            for r in board:
                if word in r:
                    return True
            return False
        def find(m, n, used, k):
            print(k)
            used.append((m, n))
            if k == len(word) - 1:
                if m > 0 and (m-1, n) not in used and board[m-1][n] == word[k]:
                    return True
                if m < row - 1 and (m+1, n) not in used and board[m+1][n] == word[k]:
                    return True
                if n > 0 and (m, n-1) not in used and board[m][n-1] == word[k]:
                    return True
                if n < col - 1 and (m, n+1) not in used and board[m][n+1] == word[k]:
                    return True
                return False
            else:
                if m > 0 and (m-1, n) not in used and board[m-1][n] == word[k]:
                    if find(m-1, n, used, k + 1):
                        return True
                    else:
                        used = used[:k]
                if m < row - 1 and (m+1, n) not in used and board[m+1][n] == word[k]:
                    if find(m+1, n, used, k + 1):
                        return True
                    else:
                        used = used[:k]
                if n > 0 and (m, n-1) not in used and board[m][n-1] == word[k]:
                    if find(m, n-1, used, k + 1):
                        return True
                    else:
                        used = used[:k]
                if n < col - 1 and (m, n+1) not in used and board[m][n+1] == word[k]:
                    if find(m, n+1, used, k + 1):
                        return True
                    else:
                        used = used[:k]
                return False
        for m in range(row):
            for n in range(col):
                if board[m][n] == word[0]:
                    if find(m, n, [], 1):
                        return True
        return False

if __name__ == '__main__':
    sol = Solution()
    board = [
  ['A','B','C','E'],
  ['S','F','E','S'],
  ['A','D','E','E']
]
    print(sol.exist(board, "ABCESEEEFS"))

