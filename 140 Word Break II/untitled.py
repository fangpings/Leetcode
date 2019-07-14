class Solution:
    def wordBreak(self, s, wordDict):
        wordDict = set(wordDict)
        self.checked = [(False, []) for _ in range(len(s) + 1)]
        def rec(k):
            tmp = []
            for word in wordDict:
                l = len(word)
                if s[k:k+l] == word:
                    if k + l == len(s):
                        tmp.append(word)
                    else:
                        if not self.checked[k + l][0]:
                            rec(k + l)
                        tmp += [word + ' ' + subs for subs in self.checked[k + l][1]]
            self.checked[k] = (True, tmp)
        rec(0)
        return self.checked[0][1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
    print(sol.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))