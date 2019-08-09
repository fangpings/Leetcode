class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator < 0 and denominator > 0:
            numerator *= -1
            sign = -1
        elif numerator > 0 and denominator < 0:
            denominator *= -1
            sign = -1
        elif numerator < 0 and denominator < 0:
            denominator *= -1
            numerator *= -1
            sign = 1
        else:
            sign = 1
        q = numerator // denominator
        r = numerator % denominator
        if r == 0:
            return str(q) if sign == 1 else '-' + str(q)
        decimal = []
        remnants = [r]
        r *= 10
        while True:
            tmp = ''
            while r // denominator == 0:
                r *= 10
                tmp += '0'
            tmp += str(r // denominator)
            r = r % denominator
            decimal.append(tmp)
            if r == 0:
                ret = str(q) + '.' + ''.join(decimal)
                return ret if sign == 1 else '-' + ret
            elif r in remnants:
                index = remnants.index(r)
                ret = str(q) + '.' + ''.join(decimal[:index]) + '(' + ''.join(decimal[index:]) + ')'
                return ret if sign == 1 else '-' + ret 
            else:
                remnants.append(r)
            r *= 10

if __name__ == '__main__':
    sol = Solution()
    print(sol.fractionToDecimal(-50,8))
