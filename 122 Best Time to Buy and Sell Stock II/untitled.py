class Solution:
    def maxProfit(self, prices):
        prices = [100000] + prices
        profit = 0
        i = 0
        while i < len(prices):
            while i + 1 < len(prices) and prices[i] >= prices[i+1]:
                i += 1
            buy = prices[i]
            while i + 1 < len(prices) and prices[i] < prices[i+1]:
                i += 1
            profit += prices[i] - buy
            i += 1
        return profit

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([7,6,4,3,1]))