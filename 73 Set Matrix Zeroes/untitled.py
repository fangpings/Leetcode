class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix == []:
            return 
        m, n = len(matrix), len(matrix[0])
        row = {}
        column = {}
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = 1
                    column[j] = 1

        for i in row.keys():
            for j in range(n):
                matrix[i][j] = 0

        for j in column.keys():
            for i in range(m):
                matrix[i][j] = 0 

if __name__ == '__main__':
    a = [[]]

    sol = Solution()
    sol.setZeroes(a)
    print(a)

