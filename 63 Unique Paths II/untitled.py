class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m-1, -1, -1):
            if obstacleGrid[i][-1]:
                break
            dp[i][-1] = 1
        for i in range(n-1, -1, -1):
            if obstacleGrid[-1][i]:
                break
            dp[-1][i] = 1
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                right = 0 if obstacleGrid[i][j+1] else dp[i][j+1]
                down = 0 if obstacleGrid[i+1][j] else dp[i+1][j]
                dp[i][j] = right + down
        return dp[0][0]

if __name__ == '__main__':
    sol = Solution()
    a = [[0,0,0,1,0,0]
]
    print(sol.uniquePathsWithObstacles(a))