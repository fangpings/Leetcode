class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.m = len(grid)
        if not self.m:
            return 0
        self.n = len(grid[0])
        if not self.n:
            return 0
        self.visited = [[0 for _ in range(self.n)] for _ in range(self.m)]
        self.grid = grid
        ret = 0
        for i in range(self.m):
            for j in range(self.n):
                ret = max(ret, self.bfs(i, j))
        return ret     
    
    def bfs(self, i, j):
        if self.visited[i][j] or not self.grid[i][j]:
            return 0
        ret = 1
        self.visited[i][j] = 1
        if i > 0:
            ret += self.bfs(i - 1, j)
        if i < self.m - 1:
            ret += self.bfs(i + 1, j)
        if j > 0:
            ret += self.bfs(i, j - 1)
        if j < self.n - 1:
            ret += self.bfs(i, j + 1)
        return ret
        