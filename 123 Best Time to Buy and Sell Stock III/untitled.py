class Solution:
    def maxProfit(self, prices):
        dp1, dp2 = 0, 0
        min1, min2 = prices[0], prices[0]
        for i in range(1, len(prices)):
            dp1 = max(dp1, prices[i] - min1)
            min1 = min(min1, prices[i])
            dp2 = max(dp2, prices[i] - min2)
            min2 = min(min2, prices[i] - dp1)
        return dp2

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([1,2,4,2,5,7,2,4,9,0]))