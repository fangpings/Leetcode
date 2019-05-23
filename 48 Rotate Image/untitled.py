def rotate(matrix):
    l = len(matrix[0])
    if l < 2:
        return
    loops = l // 2
    l -= 1
    for i in range(loops):
        for j in range(l - 2 * i):
            matrix[i+j][l-i], matrix[l-i][l-i-j], matrix[l-i-j][i], matrix[i][i+j] = matrix[i][i+j], matrix[i+j][l-i], matrix[l-i][l-i-j], matrix[l-i-j][i]

if __name__ == '__main__':
    a = [[1,2],[3,4]]
    rotate(a)
    print(a)