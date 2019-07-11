class Solution:
    def minCut(self, s):
        dp = [0 for _ in range(len(s) + 1)]
        isPalidrome = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            tmp_min = 1000000
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - 1 <= i + 1 or isPalidrome[i+1][j-1]): 
                    isPalidrome[i][j] = True
                    tmp_min = 0 if j == len(s) - 1 else min(tmp_min, dp[j+1] + 1)
            dp[i] = tmp_min
        return dp[0]

if __name__ == '__main__':
    sol = Solution()
    print(sol.minCut("a"))



