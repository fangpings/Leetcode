class Solution:
    def climbStairs(self, n):
        stair = [0 for _ in range(n + 1)]
        stair[0] = 1
        i = 0
        while i + 2 <= n:
            stair[i+1] += stair[i]
            stair[i+2] += stair[i]
            i += 1
        stair[i+1] += stair[i]
        return stair[-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.climbStairs(1))
