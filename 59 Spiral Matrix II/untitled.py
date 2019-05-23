def generateMatrix(n):
    ret = [[0 for _ in range(n)] for _ in range(n)]
    k = 1
    layer = 0
    i = 0
    j = 0
    while layer < n // 2:
        while j < n - layer - 1:
            print(i, j)
            ret[i][j] = k
            k += 1
            j += 1
        while i < n - layer - 1:
            print(i, j)
            ret[i][j] = k
            k += 1
            i += 1
        while j > layer:
            print(i, j)
            ret[i][j] = k
            k += 1
            j -= 1
        while i > layer:
            print(i, j)
            ret[i][j] = k
            k += 1
            i -= 1
        i += 1
        j += 1
        layer += 1
    if n % 2:
        ret[n//2][n//2] = k
    return ret

if __name__ == '__main__':
    print(generateMatrix(5))