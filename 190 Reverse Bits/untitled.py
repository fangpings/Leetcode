class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret = 0
        for i in range(32):
            ret = ret << 1
            if n % 2:
                ret += 1
            n = n >> 1
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseBits(4294967293))
