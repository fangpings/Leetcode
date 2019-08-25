class Solution:
    def palindromePairs(self, words):
        dic = {word:i for i, word in enumerate(words)}
        ret = set()
        for i, w in enumerate(words):
            for j in range(len(w) + 1):
                fh = w[:j]
                sh = w[j:]
                if sh[::-1] in dic and dic[sh[::-1]] != i and fh[::-1] == fh:
                    ret.add((dic[sh[::-1]], i))
                if fh[::-1] in dic and dic[fh[::-1]] != i and sh[::-1] == sh:
                    ret.add((i, dic[fh[::-1]]))
        return list(ret)




if __name__ == '__main__':
    sol = Solution()
    print(sol.palindromePairs(["abcd","dcba","lls","s","sssll"]))






