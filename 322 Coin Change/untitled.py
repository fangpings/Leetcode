# class Solution:
#     def coinChange(self, coins, amount):
#         self.dp = [0 for _ in range(amount + 1)]
#         return self.rec(coins, amount)

#     def rec(self, coins, amount):
#         if amount < 0:
#             return -1
#         if amount == 0:
#             return 0
#         if self.dp[amount] != 0:
#             return self.dp[amount]
#         min_coins = 1000000
#         for c in coins:
#             nums = self.rec(coins, amount - c)
#             if nums != -1:
#                 min_coins = min(min_coins, nums)
#         self.dp[amount] = min_coins + 1 if min_coins != 1000000 else -1
#         return self.dp[amount]

class Solution:
    def coinChange(self, coins, amount):
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i], dp[i-c] + 1)
        return dp[amount] if dp[amount] < amount + 1 else -1
        


if __name__ == '__main__':
    sol = Solution()
    print(sol.coinChange([1,2,5], 11))

