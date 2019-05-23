def divide(a: int, b: int):
    sign = 1 if (a < 0) == (b < 0) else -1
    a, b = abs(a), abs(b)
    ret = 0
    while True:
        k = 0 
        while a >= b << (k + 1):
            k += 1
        a -= b << k
        if a < 0:
            break
        ret += 1 << k
    ret *= sign
    if ret > 2 ** 31 - 1:
        return 2 ** 31
    elif ret < - 2 ** 31:
        return - 2 ** 31
    else:
        return ret

if __name__ == '__main__':
    print(divide(0, 3))