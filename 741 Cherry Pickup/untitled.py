# class Solution(object):
#     def cherryPickup(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         forward = self.one_pass(grid)
#         if forward == -1:
#             return 0
#         new_grid = [x[::-1] for x in grid]
#         new_grid = new_grid[::-1]
#         return forward + self.one_pass(new_grid)

#     def one_pass(self, grid):
#         m = len(grid)
#         dp = [[0 for _ in range(m)] for _ in range(m)]
#         path = [[-1 for _ in range(m)] for _ in range(m)] # 1 for right, 0 for down
#         dp[-1][-1] = grid[-1][-1]
#         if grid[-1][-1] == 1:
#             grid[-1][-1] = 0
#         for j in range(m - 2, -1, -1):
#             dp[-1][j] = -1 if grid[-1][j] == -1 or dp[-1][j+1] == -1 else dp[-1][j+1] + grid[-1][j]
#             path[-1][j] = -1 if dp[-1][j] == -1 else 1
#         for i in range(m - 2, -1, -1):
#             dp[i][-1] = -1 if grid[i][-1] == -1 or dp[i+1][-1] == -1 else dp[i+1][-1] + grid[i][-1]
#             path[i][-1] = -1 if dp[i][-1] == -1 else 0
#         for i in range(m - 2, -1, -1):
#             for j in range(m - 2, -1, -1):
#                 if grid[i][j] == -1 or (dp[i][j+1] == -1 and dp[i+1][j] == -1):
#                     dp[i][j] = -1
#                     path[i][j] = -1
#                 elif dp[i][j+1] == -1 and dp[i+1][j] != -1:
#                     dp[i][j] = dp[i+1][j] + grid[i][j]
#                     path[i][j] = 0
#                 elif dp[i][j+1] != -1 and dp[i+1][j] == -1:
#                     dp[i][j] = dp[i][j+1] + grid[i][j]
#                     path[i][j] = 1
#                 else:
#                     if dp[i][j+1] > dp[i+1][j]:
#                         dp[i][j] = dp[i][j+1] + grid[i][j]
#                         path[i][j] = 1
#                     else:
#                         dp[i][j] = dp[i+1][j] + grid[i][j]
#                         path[i][j] = 0
#         if dp[0][0] == -1:
#             return -1
#         i, j = 0, 0
#         while path[i][j] != -1:
#             grid[i][j] = 0
#             if path[i][j] == 1:
#                 j += 1
#             else:
#                 i += 1
#         return dp[0][0]

class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        

if __name__ == '__main__':
    sol = Solution()
    grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
    print(sol.cherryPickup(grid))

