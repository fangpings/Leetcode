class Solution:
    def removeInvalidParentheses(self, s):
        self.ret = []
        self.remove_one(s, 0, 0, ('(', ')'))
        return self.ret

    def remove_one(self, s, last_i, last_j, bracket):
        stack = 0
        for i in range(last_i, len(s)):
            if s[i] == bracket[0]:
                stack += 1
            if s[i] == bracket[1]:
                stack -= 1
            if stack >= 0:
                continue
            for j in range(last_j, i + 1):
                if s[j] == bracket[1] and (j == last_j or s[j-1] != bracket[1]):
                    self.remove_one(s[:j] + s[j+1:], i, j, bracket) # 这里因为j位置的字符已经去掉了，所以i,j都自动+1了
            return # 我们一次只删一个，剩下的交给后面的递归去做
        s = s[::-1] # 如果没转过我们反向把左括号去了，如果转过了我们再转回来
        if bracket[0] == '(':
            self.remove_one(s, 0, 0, (')', '('))
        else:
            self.ret.append(s)

if __name__ == '__main__':
    sol = Solution()
    print(sol.removeInvalidParentheses(")("))


