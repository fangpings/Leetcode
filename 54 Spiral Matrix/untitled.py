def spiralOrder(matrix):
    m = len(matrix)
    if m == 0:
        return []
    n = len(matrix[0])
    if n == 0:
        return []
    hor, ver = n, m
    i, j = 0, 0
    ret = []
    while hor > 1 and ver > 1:
        for _ in range(hor - 1):
            ret.append(matrix[i][j])
            j += 1
        for _ in range(ver - 1):
            ret.append(matrix[i][j])
            i += 1
        for _ in range(hor - 1):
            ret.append(matrix[i][j])
            j -= 1
        for _ in range(ver - 2):
            ret.append(matrix[i][j])
            i -= 1
        ret.append(matrix[i][j])
        j += 1
        hor -= 2
        ver -= 2
    if ver == 1 and hor != 0:
        for _ in range(hor):
            ret.append(matrix[i][j])
            j += 1
    elif hor == 1 and ver != 0:
        for _ in range(ver):
            ret.append(matrix[i][j])
            i += 1
    return ret

if __name__ == '__main__':
    a = [[3], [2]]
    print(spiralOrder(a))


