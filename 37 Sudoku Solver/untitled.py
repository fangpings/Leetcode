from copy import deepcopy as dp
from collections import defaultdict

def solveSudoku(board):
    """
    Do not return anything, modify board in-place instead.
    """
    cr = [[i for i in range(1, 10)] for j in range(9)]
    cc = dp(cr)
    cb = dp(cr)
    ur = [[] for i in range(9)]
    uc = dp(ur)
    ub = dp(ur)
    p = defaultdict(list)

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == '.':
                ur[i].append(j)
                uc[j].append(i)
                ub[(i//3)*3+j//3].append((i, j))
            else:
                num = int(num)
                cr[i].remove(num)
                cc[j].remove(num)
                cb[(i//3)*3+j//3].remove(num)

    for i in range(9):
        for j in ur[i]:
            for k in cr[i]:
                if k in cc[j] and k in cb[(i//3)*3+j//3]:
                    p[i, j].append(k)

    def solve(board, p, ur, uc, ub):

        def update(i, j, num):
            ur[i].remove(j)
            uc[j].remove(i)
            ub[(i//3)*3+j//3].remove((i, j))
            for m in ur[i]:
                if num in p[i, m]:
                    p[i, m].remove(num)
            for n in uc[j]:
                if num in p[n, j]:
                    p[n, j].remove(num)
            for m, n in ub[(i//3)*3+j//3]:
                if num in p[m, n]:
                    p[m, n].remove(num)

        while len(p.keys()) > 0:
            i, j = sorted(list(p.keys()), key=lambda x: len(p[x]))[0]
            candidate = p.pop((i, j))
            if len(candidate) == 1:
                num = candidate[0]
                board[i][j] = str(num)
                update(i, j, num)
            elif len(candidate) == 0:
                return False
            else:
                new_p = dp(p)
                new_ur = dp(ur)
                new_uc = dp(uc)
                new_ub = dp(ub)
                for num in candidate:
                    board[i][j] = str(num)
                    update(i, j, num)
                    if solve(board, p, ur, uc, ub):
                        return True
                    p = dp(new_p)
                    ur = dp(new_ur)
                    uc = dp(new_uc)
                    ub = dp(new_ub)
                return False
        return True
    solve(board, p, ur, uc, ub)
                

if __name__ == '__main__':
    a = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    solveSudoku(a)
    print(a)







