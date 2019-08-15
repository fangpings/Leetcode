class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        self.grid = grid
        self.checked = [[0 for _ in range(n)] for _ in range(m)]
        self.ret = 0
        for i in range(m):
            for j in range(n):
                if self.check(i, j):
                    self.ret += 1
        return self.ret

    def check(self, i, j):
        if i >= 0 and j >= 0 and i < len(self.checked) and j < len(self.checked[0]) and self.grid[i][j] == '1' and not self.checked[i][j]:
            self.checked[i][j] = 1
            self.check(i+1, j)
            self.check(i, j+1)
            self.check(i-1, j)
            self.check(i, j-1)
            print(self.checked)
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))
