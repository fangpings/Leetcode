# class Solution:
#     def maximalRectangle(self, matrix):
#         m = len(matrix)
#         if m == 0:
#             return 0
#         n = len(matrix[0])
#         if n == 0:
#             return 0
#         dp = [[[(0, 0)] for _ in range(n)] for _ in range(m)]
#         if matrix[0][0] == '1':
#             dp[0][0] = [(1, 1)]
#         for i in range(1, m):
#             if matrix[i][0] == '1':
#                 dp[i][0] = [(dp[i-1][0][0][0] + 1, 1)]
#         for j in range(1, n):
#             if matrix[0][j] == '1':
#                 dp[0][j] = [(1, dp[0][j-1][0][1] + 1)]
#         for i in range(1, m):
#             for j in range(1, n):
#                 if matrix[i][j] == '1':
#                     candidate = [(1, 1)]
#                     for left_m, left_n in dp[i][j-1]:
#                         for up_m, up_n in dp[i-1][j]:
#                             candidate.append((min(left_m, up_m+1), left_n + 1))
#                             candidate.append((up_m + 1, min(left_n+1, up_n)))
#                             if left_m == 1 and up_n == 1:
#                                 continue
#                             else:
#                                 candidate.append((min(up_m + 1, left_m + 1 if left_m == 1 else left_m), min(left_n+1, up_n + 1 if up_n == 1 else up_n)))
#                     tmp_max = 0
#                     tmp = []
#                     for p, q in candidate:
#                         if p * q > tmp_max:
#                             tmp_max = p * q
#                             tmp = [(p, q)]
#                         elif p * q == tmp_max and (p, q) not in tmp:
#                             tmp.append((p, q))
#                     dp[i][j] = tmp
#         area = [[x[0][0] * x[0][1] for x in row] for row in dp]
#         for row in dp:
#             print(row)
#         return max([max(x) for x in area])

class Solution:
    def maximalRectangle(self, matrix):
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        heights = [0 for _ in range(n + 1)]
        ret = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            stack = [-1]
            for i in range(len(heights)):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    ret = max(ret, h * w)
                stack.append(i)
        return ret


if __name__ == '__main__':
    sol = Solution()
    matrix = [["0","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0"],["1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","0","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1"],["1","1","1","0","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1"],["1","0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0"],["0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1"],["1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],["0","1","1","0","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1"],["1","1","1","1","1","1","1","1","0","1","1","0","1","1","0","1","1","1","1"],["1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","0","1","1","1"]]
    for row in matrix:
        print(row)
    print(sol.maximalRectangle(matrix))

