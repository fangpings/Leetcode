class Solution:
    def partition(self, s):
        self.mapping = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        def rec(start):
            ret = []
            for i in range(start, len(s)):
                if self.mapping[start][i] == -1:
                    tmp = s[start:i+1]
                    if tmp == tmp[::-1]:
                        self.mapping[start][i] = 1      
                    else:
                        self.mapping[start][i] = 0
                if self.mapping[start][i] == 1:
                    if i == len(s) - 1:
                        ret.append([s[start:]])
                    else:
                        ret += [[s[start:i+1]] + x for x in rec(i+1)]
            return ret
        return rec(0)

if __name__ == '__main__':
    sol = Solution()
    print(sol.partition('aab'))



