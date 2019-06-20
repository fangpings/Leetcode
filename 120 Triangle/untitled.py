class Solution:
    def minimumTotal(self, triangle):
        l = len(triangle)
        if l == 1:
            return triangle[0][0]
        tmp = triangle[-1]
        for k in range(l - 2, -1, -1):
            print(tmp)
            tmp = [triangle[k][i] + min(tmp[i], tmp[i+1]) for i in range(k + 1)]
        return tmp[0]

if __name__ == '__main__':
    sol = Solution()
    a = [
     [2]
]
    print(sol.minimumTotal(a))
