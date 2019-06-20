class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        ret = [[1]]
        for k in range(1, numRows):
            tmp = [1]
            for i in range(1, k):
                tmp.append(ret[-1][i] + ret[-1][i-1])
            tmp.append(1)
            ret.append(tmp)
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.generate(1))