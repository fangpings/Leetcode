### 560 Subarray Sum Equals K

Given an array of integers and an integer **k**, you need to find the total number of continuous subarrays whose sum equals to **k**.

**Example 1:**

```
Input:nums = [1,1,1], k = 2
Output: 2
```

**Note:**

1. The length of the array is in range [1, 20,000].
2. The range of numbers in the array is [-1000, 1000] and the range of the integer **k** is [-1e7, 1e7].

### 想法

这道题也和脑筋急转弯似的。。

最核心的想法是这样的：**m到n的连续和相当于0到n的连续和减掉0到m的连续和。**

我们先把所有[0, k]的连续和存到一个defaultdict里面，用defaultdict是方便计算重复的连续和的次数。然后我们先记录一下`count = hashtable[k]`，把所有0到m等于K的连续和个数给加上去。

然后我们开始做减法，依然从0开始加连续和，只不过每加一个，**就从defaultdict里面减掉这个连续和，这是防止出现0到m的连续和减掉0到n的连续和等于K这种情况**。然后我们再看当前连续和s加上K之后在hashtable里面的个数，这就是当前位置m开始连续和等于K的个数。

