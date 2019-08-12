class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        row, column = len(dungeon), len(dungeon[0])
        dp = [[0 for _ in range(column)] for _ in range(row)]
        dp[-1][-1] = max(1 - dungeon[-1][-1], 1)
        for i in range(row - 2, -1, -1):
            dp[i][-1] = max(dp[i+1][-1] - dungeon[i][-1], 1)
        for j in range(column - 2, -1, -1):
            dp[-1][j] = max(dp[-1][j+1] - dungeon[-1][j], 1)
        for i in range(row - 2, -1, -1):
            for j in range(column - 2, -1, -1):
                right = max(dp[i][j+1] - dungeon[i][j], 1)
                down = max(dp[i+1][j] - dungeon[i][j], 1)
                dp[i][j] = min(right, down)
        return dp[0][0]

if __name__ == '__main__':
    sol = Solution()
    board = [[0]]
    # board = [[-2,-3,3], [-5, -10, 1], [10, 30, -5]]
    print(sol.calculateMinimumHP(board))
