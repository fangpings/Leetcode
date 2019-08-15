class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        mask = 1
        for i in range(32):
            if n & mask != 0:
                ret += 1
            mask = mask << 1
        return ret


if __name__ == '__main__':
    sol = Solution()
    print(sol.hammingWeight(8))