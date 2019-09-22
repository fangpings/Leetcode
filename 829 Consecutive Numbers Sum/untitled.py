from math import sqrt
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        upper = int((-1 + sqrt(1+8*N))/2)
        ret = 0
        for i in range(1, upper + 1):
            if (2*N+i-i**2) % (2*i) == 0:
                ret += 1
        return ret
        