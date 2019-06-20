class Solution:
    def maxProfit(self, prices):
        profit = 0
        buy = 1000000
        for p in prices:
            if p < buy:
                buy = p
            elif p > buy and p - buy > profit:
                profit = p - buy
        return profit

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([7,6,4,3,1]))

