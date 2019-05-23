class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 0:
            return 0
        self.n = n
        self.ret = 0
        self.dfs([], [], [])
        return self.ret

    def dfs(self, columns, xpy, xmy):
        y = len(columns)
        if y == self.n:
            self.ret += 1
            return
        for x in range(self.n):
            if x not in columns and x + y not in xpy and x - y not in xmy:
                self.dfs(columns + [x], xpy + [x + y], xmy + [x - y])

if __name__ == '__main__':
    sol = Solution()
    print(sol.totalNQueens(5))
