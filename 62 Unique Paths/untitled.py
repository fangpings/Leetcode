class Solution:
    def uniquePaths(self, m, n):
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m-1, -1, -1):
            dp[i][-1] = 1
        for i in range(n-1, -1, -1):
            dp[-1][i] = 1
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i][j+1] + dp[i+1][j]
        return dp[0][0]
