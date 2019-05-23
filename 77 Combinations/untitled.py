class Solution:
    def combine(self, n, k):
        if k == 0 or n == 0 :
            return []
        def rec(start, k):
            if k == 1:
                return [[i] for i in range(start, n + 1)]
            ret = []
            for i in range(start, n - k + 2):
                ret += [[i] + x for x in rec(i + 1, k - 1)]
            return ret
        return rec(1, k)

if __name__ == '__main__':
    sol = Solution()
    print(sol.combine(3, 2))
