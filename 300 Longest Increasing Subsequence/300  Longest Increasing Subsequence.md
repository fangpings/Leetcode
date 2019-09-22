### 300  Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

**Example:**

```
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
```

**Note:** 

- There may be more than one LIS combination, it is only necessary for you to return the length.
- Your algorithm should run in O(*n2*) complexity.

**Follow up:** Could you improve it to O(*n* log *n*) time complexity?

### 想法

O(N^2)的做法怎么样都行。。一个办法就是用DP

```python
dp[j] = max(dp[i] for i in range(j - 1) if nums[i] < nums[j]) + 1
```

要做到o(nlogn)就有点变态了。。

我们设置一个`tail`数组，`tail[i]`储存所有长度为`i+1`的递增序列的**最后一位的最小值**

```
len = 1   :      [4], [5], [6], [3]   => tails[0] = 3
len = 2   :      [4, 5], [5, 6]       => tails[1] = 5
len = 3   :      [4, 5, 6]            => tails[2] = 6
```

于是`tail`一定是递增的（因为所有的i+1位一定大于i位，所以所有i+1位的最小值一定大于所有i位的最小值）

**所以我们可以考虑使用二分查找了**

每次我们只做两件事情，如果当前元素比tail中的所有元素都大，那么说明他至少可以接在某一个当前已经发现的最长递增序列（长度为i)之后，那么我们把它append到`tail`的最后。否则，如果`tail[i-1] < x <= tails[i]`,说明x可以替换以`tail[i]`结束的那个长度为i的序列的最后一位。注意这里可能会问，既然替换了那为什么这个序列的长度不会上升一位，例如把`tail[i]`接在当前元素之后？那是因为原来的`tail[i]`在当前位置之前，没办法作为子序列的。

这个太绕了。。真不知道是怎么想出来的。。你让我解释我也没办法解释