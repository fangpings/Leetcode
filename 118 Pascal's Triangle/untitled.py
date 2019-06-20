class Solution:
    def generate(self, numRows):
        numRows += 1
        pre = [1]
        for k in range(1, numRows):
            tmp = [1]
            for i in range(1, k):
                tmp.append(pre[i] + pre[i-1])
            tmp.append(1)
            pre = tmp
        return pre

if __name__ == '__main__':
    sol = Solution()
    print(sol.generate(1))