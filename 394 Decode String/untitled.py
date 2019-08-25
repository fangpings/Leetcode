class Solution:
    def decodeString(self, s: str) -> str:
        return self.rec(s, -1)[0]

    def rec(self, s, k):
        ret = ''
        i = k + 1
        while i < len(s):
            if s[i].isdigit():
                j = i
                while s[j].isdigit():
                    j += 1
                times = int(s[i:j])
                tmp_s, pos = self.rec(s, j)
                ret += times * tmp_s
                i = pos + 1
            elif s[i].isalpha():
                ret += s[i]
                i += 1
            else:
                return ret, i
        return ret, i

if __name__ == '__main__':
    sol = Solution()
    print(sol.decodeString("1[a2[b3[c]]]"))
