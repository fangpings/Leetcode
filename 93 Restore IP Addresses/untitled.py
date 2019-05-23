class Solution:
    def restoreIpAddresses(self, s):
        l = len(s)
        if l < 4 or l > 16:
            return []
        dp = [[] for _ in range(l)]
        dp += [[('', 0)]]
        for i in range(l - 1, -1, -1):
            if s[i] == '0':
                dp[i] = [(s[i] + '.' + x, y + 1) for x, y in dp[i+1] if y <= 3]
            elif s[i] == '1':
                dp[i] += [(s[i] + '.' + x, y + 1) for x, y in dp[i+1] if y <= 3]
                if i + 1 < l:
                    dp[i] += [(s[i:i+2] + '.' + x, y + 1) for x, y in dp[i+2] if y <= 3]
                if i + 2 < l:
                    dp[i] += [(s[i:i+3] + '.' + x, y + 1) for x, y in dp[i+3] if y <= 3]
            elif s[i] == '2':
                dp[i] += [(s[i] + '.' + x, y + 1) for x, y in dp[i+1] if y <= 3]
                if i + 1 < l:
                    dp[i] += [(s[i:i+2] + '.' + x, y + 1) for x, y in dp[i+2] if y <= 3]
                if i + 2 < l and (s[i+1] < '5' or s[i+1] == '5' and s[i+2] <= '5'):
                    dp[i] += [(s[i:i+3] + '.' + x, y + 1) for x, y in dp[i+3] if y <= 3]
            else:
                dp[i] += [(s[i] + '.' + x, y + 1) for x, y in dp[i+1] if y <= 3]
                if i + 1 < l:
                    dp[i] += [(s[i:i+2] + '.' + x, y + 1) for x, y in dp[i+2] if y <= 3]
        return [x[:-1] for x, y in dp[0] if y == 4]

if __name__ == '__main__':
    sol = Solution()
    print(sol.restoreIpAddresses(''))
