class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        if k > len(prices) // 2:
            profit = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    profit += prices[i] - prices[i-1]
            return profit
        dp = [0 for _ in range(k + 1)]
        mink = [prices[0] for _ in range(k + 1)]
        for i in range(1, len(prices)):
            for j in range(1, k + 1):
                mink[j] = min(mink[j], prices[i] - dp[j-1])
                dp[j] = max(dp[j], prices[i] - mink[j])
        return dp[-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit(2, [3,3,5,0,0,3,1,4]))