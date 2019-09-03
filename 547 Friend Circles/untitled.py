class Solution:
    def findCircleNum(self, M): 
        self.M = M
        self.n = len(M)
        self.visited = [0 for _ in range(self.n)]
        count = 0
        for i in range(self.n):
            if not self.visited[i]:
                count += 1
                self.search_col(i)
        return count

    def search_col(self, i):
        if not self.visited[i]:
            self.visited[i] = 1
            for j in range(self.n):
                if self.M[i][j]:
                    self.search_col(j)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findCircleNum([[1]]))