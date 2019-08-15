### 123 Best Time to Buy and Sell Stock III

Say you have an array for which the *i*th element is the price of a given stock on day *i*.

Design an algorithm to find the maximum profit. You may complete at most *two*transactions.

**Note:** You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

**Example 1:**

```
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
```

**Example 2:**

```
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
```

**Example 3:**

```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

#### 想法

首先说一下好理解的DP.

```
dp[k, i] = max(dp[k, i-1], prices[i] - prices[j] + dp[k-1, j-1]), j=[0..i-1]
```

这里k是最多进行k次transaction，i是第i天，最后return `dp[-1][-1]`。相当于要么取前一天的结果(即今天不做交易)，要么今天卖掉第j天买进的股票，然后取前j-1天的k-1次交易的最大值。

可以改写成这样(注意下标全部从1开始)
$$
dp[k,i\geq1]=\max_{i}(dp[k, i-1], \max_{j=[0,...,i-1]}(prices[i] - prices[j] + dp[k-1, j-1]))\\
dp[k,0] = 0
$$
继续改写，可以改写成这样
$$
dp[k,i\geq1]=\max_{i}(dp[k, i-1], prices[i] - \min_{j=[0,...,i-1]}(prices[j] - dp[k-1, j-1]))\\
dp[k,0]=0
$$
那按照这个公式写出的代码类似于这样

```python
dp = [[0 for _ in range(len(prices))] for _ in range(transactions + 1)]
for k in range(1, transactions + 1):
  	for i in range(1, len(prices)):
      	minj = prices[0]  # 因为当j=0的时候没办法取dp[k-1][j-1]
      	for j in range(1,i):
          	minj = min(minj, prices[j] - dp[k-1][j-1])
        dp[k][i] = max(dp[k][i-1], prices[i] - minj)
```

然后我们发现最里面的j循环是多余的(因为内层循环相当于找到到i-1位置的最小值，我们在循环i的时候可以顺便找了，每次更新i的时候和之前找到的最小值做比较就行了），于是我们可以继续改写

```python
dp = [[0 for _ in range(len(prices))] for _ in range(transactions + 1)]
for k in range(1, transactions):
  	minj = prices[0]
  	for i in range(1, len(prices)):
        dp[k][i] = max(dp[k][i-1], prices[i] - minj)
        minj = min(minj, prices[i] - dp[k-1][i-1])  # 根据上面的代码minj应该对应到i-1的最小值，那我们先算dp[k][i]再更新minj，不过试了一下这条的顺序好像不影响
```

这时候时间复杂度已经降到O(kn)了,空间复杂度也是O(kn)，但是还有下降空间，我们把内外层循环换一下，这时候要保存mink数组了，否则要乱套的

```python
dp = [[0 for _ in range(len(prices))] for _ in range(transactions + 1)]
mink = [prices[0] for _ in range(transactions + 1)]
for i in range(1, len(prices)):
		for k in range(1, transactions + 1):
				dp[k][i] = max(dp[k][i-1], prices[i] - mink[k])
        mink[k] = min(mink[k], prices[i] - dp[k-1][i-1])
```

我们发现内层循环是独立于外层的，而且外层的第i步只依赖于外层的第i-1步，所以我们没必要继续保存second dimension的i了，直接删掉就行

```python
dp = [0 for _ in range(transactions + 1)]
mink = [prices[0] for _ in range(transactions + 1)]
for i in range(1, len(prices)):
		for k in range(1, transactions + 1):
				dp[k] = max(dp[k], prices[i] - mink[k])
        mink[k] = min(mink[k], prices[i] - dp[k-1])
```

现在是k=2，那我们内层循环也不需要了，保存4个变量即可

```python
dp1, dp2 = 0, 0
min1, min2 = prices[0], prices[0]
for i in range(1, len(prices)):
  	dp1 = max(dp1, prices[i] - min1)
    min1 = min(min1, prices[i])
    dp2 = max(dp2, prices[i] - min2)
    min2 = min(min2, prices[i] - dp1)
return dp2
```

其实最后这个写法还有另外一种解释，但我实在没看懂。这种方法虽然好懂，但是是在复杂的dp的基础上一步一步优化下来的，也不失为一个好办法。

最后，在实际做的时候碰到了内存过大的问题。当交易次数很大的时候，保存的数组也容易过大。这个时候我们考虑一下，如果交易次数大于总交易天数的一半，那么说明我们每两天都可以做一次交易，即只要看到价格差我们就可以赚钱，这个时候就不用保存任何数组了。

```python
if k > len(prices) // 2:
		profit = 0
		for i in range(1, len(prices)):
				if prices[i] > prices[i-1]:
						profit += prices[i] - prices[i-1]
return profit
```

