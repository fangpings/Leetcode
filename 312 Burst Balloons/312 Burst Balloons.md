### 312 Burst Balloons

Given `n` balloons, indexed from `0` to `n-1`. Each balloon is painted with a number on it represented by array `nums`. You are asked to burst all the balloons. If the you burst balloon `i` you will get `nums[left] * nums[i] * nums[right]` coins. Here `left` and `right` are adjacent indices of `i`. After the burst, the `left` and `right` then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

**Note:**

- You may imagine `nums[-1] = nums[n] = 1`. They are not real therefore you can not burst them.
- 0 ≤ `n` ≤ 500, 0 ≤ `nums[i]` ≤ 100

**Example:**

```
Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
```

### 想法

面试要是出这题说明人家压根就不想要你。。

最开始最naive的就是O(N!)的做法，每次pop每一个，再试N-1的情况。稍微改进一下我们发现，比如我们pop出135之后，剩下的元素和这三个pop出去的顺序是没关系的，所以我们pop相当于一个permutation，每个permutation只需要计算一个最终结果，差不多能把复杂度改进到O(2^N)，但是还是不可接受。

我们考虑问题出在哪里，最大的问题是，一个元素pop之后，剩下的和他相邻的元素他的边界就变了，于是我们不能重新利用已经有的信息。那什么时候是不变的呢，那就是**只剩最后一个元素的时候，它两边的元素永远都是1**。然后如果我们选定一个最后pop的元素，那么它左右(`nums[:index]`和`nums[index+1:]`的所有元素，他们的左右最远边界也确定了，就是他自己和1。**于是我们看到了不变的东西！**再加上这是一个bottom-up的性质，于是我们考虑用DP（这种DP他妈的哪个人想得到）。

我们令`dp[i][j]`为把`i`到`j`burst出去所能拿到的最大点数(includsive)，那么我们要求的就是`dp[1][n-1]`（我们已经在原数组两边pad 1了）根据上面的想法，我们应该挑一个最后pop的，那么`dp[i][j] = max(dp[i][k] + dp[k+1][j] + nums[k]*nums[i-1]*nums[k+1] for k in range(i, j+1))`。即循环ij范围内的每一个元素，把他作为最后一个pop的元素，然后计算当他是最后一个pop的时候，他左右的元素`dp[i][k]`和`dp[k+1][j]`的值（根据我们上面的分析，这两个范围的边界都已经确定了，所以是可以计算的），然后我们取最大值就可以了。这样我们就把问题分成了一样的两个子问题，这也是分治的想法