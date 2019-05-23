class Solution:
    def grayCode(self, n):
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        first_half = self.grayCode(n-1)
        second_half = [2 ** (n - 1) + x for x in first_half[::-1]]
        return first_half + second_half

if __name__ == '__main__':
    sol = Solution()
    print(sol.grayCode(4))

