def getPermutation(n, k):
    factor = 1
    k -= 1
    candidate = [i for i in range(1, n+1)]
    for i in range(1, n + 1):
        factor *= i
    ret = ''
    for i in range(n, 0, -1):
        factor = int(factor / i)
        sel = int(k // factor)
        ret += str(candidate.pop(sel))
        k = int(k % factor)
    return ret

if __name__ == '__main__':
    print(getPermutation(2, 2))