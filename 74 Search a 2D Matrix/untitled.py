class Solution:
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        row_start = [row[0] for row in matrix]

        left, right = 0, m - 1
        while left <= right:
            mid = (left + right) // 2
            if row_start[mid] == target:
                return True
            if row_start[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if left == 0:
            return False
        target_row = matrix[left-1]
        if target_row[-1] < target:
            return False
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if target_row[mid] == target:
                return True
            if target_row[mid] > target:
                right = mid - 1
            else:
                left = mid + 1 
        return False         

if __name__ == '__main__':
    a = [[1,2,3]]
    sol = Solution()
    print(sol.searchMatrix(a, 2))

