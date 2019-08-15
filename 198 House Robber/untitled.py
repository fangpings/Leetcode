class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        if len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        dp = [0 for _ in range(len(nums))]
        dp[-1] = nums[-1]
        dp[-2] = nums[-2]
        dp[-3] = nums[-1] + nums[-3]
        for i in range(-4, -len(nums)-1, -1):
            dp[i] = max(dp[i+2], dp[i+3]) + nums[i]
        return max(dp[0], dp[1])

if __name__ == '__main__':
    sol = Solution()
    print(sol.rob([9,1,9,1,1,9,1,9,1,9]))
