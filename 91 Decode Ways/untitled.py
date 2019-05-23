# class Solution:
#     def numDecodings(self, s):
#         self.count = 0
#         if len(s) == 0:
#             return 0
#         self.rec(s)
#         return self.count

#     def rec(self, s):
#         if len(s) == 0:
#             self.count += 1
#             return
#         if s[0] == '0':
#             return
#         if len(s) > 1 and (s[0] == '1' or (s[0] == '2' and s[1] <= '6')):
#                 self.rec(s[1:])
#                 self.rec(s[2:])
#         else:
#             self.rec(s[1:])

class Solution:
    def numDecodings(self, s):
        if len(s) == 0:
            return 0
        dp = [0 for _ in range(len(s) + 1)]
        dp[-1] = 1
        dp[-2] = 1 if s[-1] != '0' else 0
        for i in range(len(s) - 2, -1, -1):
            if s[i] != '0':
                if s[i] == '1' or (s[i] == '2' and s[i+1] <= '6'):
                    dp[i] = dp[i+1] + dp[i+2]
                else:
                    dp[i] = dp[i+1]
        return dp[0]

if __name__ == '__main__':
    sol = Solution()
    print(sol.numDecodings(""))
