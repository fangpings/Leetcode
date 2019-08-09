### 162 Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array `nums`, where `nums[i] ≠ nums[i+1]`, find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that `nums[-1] = nums[n] = -∞`.

**Example 1:**

```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

**Example 2:**

```
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
```

**Note:**

Your solution should be in logarithmic complexity.

### 想法

这道题难的一点就是要在log时间复杂度内解决。

注意到这一点，**那就是Peak元素只会在连续的Ascending序列和Descending序列交界的地方出现，所以如果我们的当前位置是Ascending(`nums[i] < nums[i+1]`)，我们在右边肯定能找到一个Peak(这种比较方法下不包括`i`），同理如果当前位置是Descending的(`nums[i] < nums[i+1]`)，我们在左边肯定能找到一个Peak(这种比较方法下包括`i`)。相当于我们缩小了查找范围，因为题目只需要我们找到一个Peak就行，而在缩小的范围内我们保证有一个Peak。**我们这样做直到`left == right`即可。