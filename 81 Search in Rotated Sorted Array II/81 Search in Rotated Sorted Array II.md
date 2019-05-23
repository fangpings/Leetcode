### 81 Search in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., `[0,0,1,2,2,5,6]` might become `[2,5,6,0,0,1,2]`).

You are given a target value to search. If found in the array return `true`, otherwise return `false`.

**Example 1:**

```
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
```

**Example 2:**

```
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
```

**Follow up:**

- This is a follow up problem to [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/description/), where `nums` may contain duplicates.
- Would this affect the run-time complexity? How and why?

#### 想法

这时候Worst Time Complexity肯定变成O(N)，考虑`[1,1,1,1,1]`这种，`low`,`high`和`mid`全部相等，这时候没法判断到底在哪个区间里面。

这个时候我们要在做二分之前加一条

```python
while low < high and nums[low] == nums[high]:
    low += 1
```

碰到这种`nums[low] == nums[high]`的情况，这种时候我们要避免`low`和`high`重复，我们要保证`low`和`high`至少是不一样的，这样**我们在每次新区间的时候至少会引入一个不同的数字来实现查找**。另外注意这一步的判断条件是`low < high`而主循环的判断条件是`low <= high`，这一条在只剩一个数字的时候很关键，即例如输入就是`[1]`这种情况。这种情况下我们不需要做多余的重复判断了。