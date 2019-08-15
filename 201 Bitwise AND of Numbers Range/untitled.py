class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        move = 0
        while m != n:
            m >>= 1
            n >>= 1
            move += 1
        return m << move

if __name__ == '__main__':
    sol = Solution()
    print(sol.rangeBitwiseAnd(5, 7))