INT_MAX = 1000000
from collections import deque

class Solution:
    def shortestDistance(self, grid):
        self.grid = grid
        self.m = len(grid)
        if not self.m:
            return -1
        self.n = len(grid[0])
        if not self.n:
            return -1
        self.board = [[[] for _ in range(self.n)] for _ in range(self.m)]
        k = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    k += 1
                    self.bfs(i, j, k)
        ret = INT_MAX
        print(self.board)
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0:
                    if len(self.board[i][j]) == k:
                        ret = min(ret, sum(self.board[i][j]))
        if ret == INT_MAX:
            return -1
        return ret
                        

    def bfs(self, i, j, k):
        queue = deque()
        queue.appendleft((i, j))
        self.board[i][j].append(0)
        self.visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        self.visited[i][j] = True
        while queue:
            m, n = queue.pop()
            path = self.board[m][n][-1]
            if m > 0 and not self.visited[m-1][n] and self.grid[m-1][n] == 0:
                self.board[m-1][n].append(path + 1)
                queue.appendleft((m-1, n))
                self.visited[m-1][n] = True
            if m < self.m - 1 and not self.visited[m+1][n] and self.grid[m+1][n] == 0:
                self.board[m+1][n].append(path + 1)
                queue.appendleft((m+1, n))
                self.visited[m+1][n] = True
            if n > 0 and not self.visited[m][n-1] and self.grid[m][n-1] == 0:
                self.board[m][n-1].append(path + 1)
                queue.appendleft((m, n-1))
                self.visited[m][n-1] = True
            if n < self.n - 1 and not self.visited[m][n+1] and self.grid[m][n+1] == 0:
                self.board[m][n+1].append(path + 1)
                queue.appendleft((m, n+1))
                self.visited[m][n+1] = True

                    

if __name__ == '__main__':
    sol = Solution()
    print(sol.shortestDistance([[1, 2, 0]]))