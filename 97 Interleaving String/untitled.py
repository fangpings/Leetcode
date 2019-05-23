class Solution:
    def isInterleave(self, s1, s2, s3):
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        dp = [[True for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        for i in range(1, l1 + 1):
            dp[i][0] = s1[i-1] == s3[i-1] and dp[i-1][0]
        for j in range(1, l2 + 1):
            dp[0][j] = s2[j-1] == s3[j-1] and dp[0][j-1]
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.isInterleave("c", "a", "ac"))
