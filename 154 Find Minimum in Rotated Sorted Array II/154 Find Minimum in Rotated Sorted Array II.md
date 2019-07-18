### 154 Find Minimum in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  `[0,1,2,4,5,6,7]` might become  `[4,5,6,7,0,1,2]`).

Find the minimum element.

The array may contain duplicates.

**Example 1:**

```
Input: [1,3,5]
Output: 1
```

**Example 2:**

```
Input: [2,2,2,0,1]
Output: 0
```

**Note:**

- This is a follow up problem to [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/).
- Would allow duplicates affect the run-time complexity? How and why?

### 想法

这种带重复的rotated，最关键的是这一句了。这句保证`left == right == mid`的情况下程序依然可以正确的处理。

```python
while low < high - 1 and nums[low] == nums[high]:
		low += 1
```

然后剩下的和二分查找差不多。想法就是如果左中右的大小关系正确`left <= mid <= right`那么说明现在已经是正确排序了，返回`left`就行。如果左右区间有一个错了，说明最小值应该在错的区间里面。但是这个时候区间应该包括两个端点（不知道谁是大谁是小），所以更新策略应当是`right = mid`或者`low = mid`，那么相对应的循环结束的条件应当是`low < high - 1`（其实这一点我也没太弄明白是为啥）

