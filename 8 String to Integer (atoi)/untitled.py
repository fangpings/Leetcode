def myAtoi(s: str) -> int:
    s = s.strip()
    sign = 1
    maxint = 2147483647
    minint = -2147483648
    try:
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        output = 0
        for c in s:
            if not ('0' <= c <= '9'):
                break
            output = output * 10 + int(c)
        output = output * sign
        if output > maxint:
            return maxint
        elif output < minint:
            return minint
        return output
    except:
        return 0

if __name__ == '__main__':
    print(myAtoi('123'), 123)
    print(myAtoi('   123'), 123)
    print(myAtoi('   -123'), -123)
    print(myAtoi('  +123'), 123)
    print(myAtoi('  123erw'), 123)
    print(myAtoi('  afdas'), 0)
    print(myAtoi('+0123'), 123)
    print(myAtoi('-91283472332'), -2147483648)

