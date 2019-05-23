def reverse(x: int) -> int:
    sign = 1 if x >= 0 else -1
    x *= sign
    output = 0
    while x > 0:
        output = output * 10 + x % 10
        x = x // 10
    output *= sign
    if output > 2**31 - 1 or output < -2**31:
        return 0
    return output

if __name__ == '__main__':
    print(reverse(123), 321)
    print(reverse(0), 0)
    print(reverse(-123), -321)
    print(reverse(120), 21)
    print(reverse(-120), -21)
    print(reverse(2**31-1))
