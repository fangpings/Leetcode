class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping1 = {}
        mapping2 = {}
        for i in range(len(s)):
            if s[i] not in mapping1:
                mapping1[s[i]] = t[i]
            elif mapping1[s[i]] != t[i]:
                return False
        for i in range(len(t)):
            if t[i] not in mapping2:
                mapping2[t[i]] = s[i]
            elif mapping2[t[i]] != s[i]:
                return False
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.isIsomorphic('ab', 'aa'))