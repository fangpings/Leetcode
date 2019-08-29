class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for k in range(0, n - 1):
            for i in range(1, n - k - 1):
                j = i + k
                for mid in range(i, j + 1):
                    dp[i][j] = max(dp[i][j], dp[i][mid-1] + nums[mid] * nums[i-1] * nums[j+1] + dp[mid+1][j])
        return dp[1][n-2]

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxCoins([3,2]))