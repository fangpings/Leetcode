class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        if m == 0 or n == 0:
            return 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = grid[-1][-1]
        for i in range(m-2, -1, -1):
            dp[i][-1] = dp[i+1][-1] + grid[i][-1]
        for i in range(n-2, -1, -1):
            dp[-1][i] = dp[-1][i+1] + grid[-1][i]
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = min(dp[i][j+1], dp[i+1][j]) + grid[i][j]
        return dp[0][0]

if __name__ == '__main__':
    sol = Solution()
    a = [[1,2,3]]
    print(sol.minPathSum(a))