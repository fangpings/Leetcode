class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t):
            count = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    count += 1
            return True if count == 1 else False
        elif abs(len(s) - len(t)) == 1:
            if len(s) > len(t):
                s, t = t, s
            flag = False
            i = 0
            while i < len(s):
                if flag:
                    if s[i] != t[i + 1]:
                        return False
                    else:
                        i += 1
                else:
                    if s[i] != t[i]:
                        flag = True
                    else:
                        i += 1
            return True
        else:
            return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.isOneEditDistance('aa', 'acd'))
