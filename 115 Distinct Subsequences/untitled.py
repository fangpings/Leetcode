class Solution:
    def numDistinct(self, s, t):
        len_s, len_t = len(s), len(t)
        if len_t > len_s or len_t == 0:
            return 0
        dp = [[0 for _ in range(len_s)] for _ in range(len_t)]
        dp[0][0] = 0 if s[0] != t[0] else 1
        for i in range(1, len_s):
            dp[0][i] = dp[0][i-1] + 1 if s[i] == t[0] else dp[0][i-1]
        for j in range(1, len_t):
            for i in range(j, len_s):
                dp[j][i] = dp[j][i-1] + dp[j-1][i-1] if s[i] == t[j] else dp[j][i-1]
        for line in dp:
            print(line)
        return dp[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.numDistinct("bagbag", "bag"))