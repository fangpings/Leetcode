### 442 Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ *n* (*n* = size of array), some elements appear **twice** and others appear **once**.

Find all the elements that appear **twice** in this array.

Could you do it without extra space and in O(*n*) runtime?

**Example:**

```
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
```

### 想法

这种数组内的值小于数组长度的统计型题目，都可以用数组自己的index做hash。对于每个值，在对应的index位置加上数组长度，因为没有值会大于等于数组长度，所以取模之后实际上不影响

```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums += [0]
        l = len(nums)
        for n in nums:
            nums[n % l] += l
        ret = []
        for i, n in enumerate(nums):
            if n // l >= 2:
                ret.append(i)
        return ret
```

