class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True
        square = 0
        log = set()
        log.add(n)
        s = str(n)
        while square not in log:
            log.add(square)
            if square == 1:
                return True
            square = sum([int(c) ** 2 for c in s])
            s = str(square)
            print(log)
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.isHappy(5))

