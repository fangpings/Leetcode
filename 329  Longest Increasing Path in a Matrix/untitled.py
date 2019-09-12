class Solution:
    def longestIncreasingPath(self, matrix):
        self.matrix = matrix
        self.m = len(matrix)
        if not self.m:
            return 0
        self.n = len(matrix[0])
        if not self.n:
            return 0

        self.dp = [[0 for _ in range(self.n)] for _ in range(self.m)]
        ret = 0
        for i in range(self.m):
            for j in range(self.n):
                if not self.dp[i][j]:
                    self.search(i, j)
                ret = max(ret, self.dp[i][j])
        return ret

    def search(self, i, j):
        if self.dp[i][j]:
            return self.dp[i][j]
        ret = 0
        if i > 0 and self.matrix[i-1][j] > self.matrix[i][j]:
            ret = max(ret, self.search(i-1, j))
        if i < self.m - 1 and self.matrix[i+1][j] > self.matrix[i][j]:
            ret = max(ret, self.search(i+1, j))
        if j > 0 and self.matrix[i][j-1] > self.matrix[i][j]:
            ret = max(ret, self.search(i, j-1))
        if j < self.n - 1 and self.matrix[i][j+1] > self.matrix[i][j]:
            ret = max(ret, self.search(i, j+1))
        self.dp[i][j] = ret + 1
        return ret + 1

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestIncreasingPath([[1],[2]]))


