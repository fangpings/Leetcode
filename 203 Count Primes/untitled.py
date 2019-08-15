class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        primes = [1 for _ in range(n + 1)]
        i = 2
        ret = 1
        while i ** 2 < n:
            j = i ** 2
            while j < n:
                primes[j] = 0
                j += i
            i += 1
            while not primes[i]:
                i += 1
            ret += 1
        ret -= 1
        while i < n:
            if primes[i]:
                ret += 1
            i += 1
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.countPrimes(3))
