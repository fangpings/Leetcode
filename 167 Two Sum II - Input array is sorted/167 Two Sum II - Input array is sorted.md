### 167 Two Sum II - Input array is sorted

Given an array of integers that is already **sorted in ascending order**, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

**Note:**

- Your returned answers (both index1 and index2) are not zero-based.
- You may assume that each input would have *exactly* one solution and you may not use the *same* element twice.

**Example:**

```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```

### 想法

这道题其实第一反应就是两个指针一个最左边一个最右边向中间移动。但是没有想通这个做法为什么不会漏掉。

想法很简单，`low`和`high`两个指针，如果`low + high == target`那就返回，如果小于，那`low += 1`,如果大于，那就`high -= 1`。

但是这个做法有一个未证明的问题就是会不会有漏掉的？换言之，如果`nums[low] + nums[high] < target`的时候，我们为什么不能选择增加`high`的index呢？`low`这个index可能并没有和`high+k`的index检测过。

这里可以证明，如果按照第二段的算法，那么如果`nums[low] + nums[high] < target`,则`nums[low] + nums[high + 1] > target`。这是因为`high + 1`这个index已经和某个小于等于`low`的index配对过了（否则不会从`high + 1`变到`high`）,我们假设这个index是`low - i`。那么这个时候我们有`nums[low - i] + nums[high + 1] > target`,因为在这个节点`high`减小了。那么肯定就有`nums[low] + nums[high + 1] > target`