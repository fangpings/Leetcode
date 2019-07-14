class Solution:
    def wordBreak(self, s, wordDict):
        self.checked = [0 for _ in range(len(s) + 1)]
        def rec(k):
            if k == len(s):
                return True
            if self.checked[k]:
                return False
            for word in wordDict:
                l = len(word)
                if s[k:k+l] == word and not self.checked[k + l]:
                    if rec(k + l):
                        return True
            self.checked[k] = 1
            return False
        return rec(0)

if __name__ == '__main__':
    sol = Solution()
    print(sol.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
    print(sol.wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"]))