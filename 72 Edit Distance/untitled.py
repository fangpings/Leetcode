class Solution:
    def minDistance(self, word1, word2):
        l1, l2= len(word1), len(word2)
        dp = [[None for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        dp[0][0] = 0 
        for i in range(1, l1 + 1):
            dp[i][0] = i
        for i in range(1, l2 + 1):
            dp[0][i] = i
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                flag = 0 if word1[i-1] == word2[j-1] else 1
                dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j] + 1, dp[i-1][j-1] + flag)
        return dp[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.minDistance('intention', 'execution'))