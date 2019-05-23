### 18 4Sum(NSum)

Given an array `nums` of *n* integers and an integer `target`, are there elements *a*, *b*, *c*, and *d* in `nums` such that *a* + *b* + *c* + *d* = `target`? Find all unique quadruplets in the array which gives the sum of `target`.

**Note:**

The solution set must not contain duplicate quadruplets.

**Example:**

```
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
```

#### 总结

对于Nsum的问题，我们可以利用递归每次将N减少1，最后归结到2Sum的问题。

```python
def NSum(nums, N, target):
    def NSum_recursive(nums, N, target):
        # nums must be sorted
        result = []
        # the following line has huge impact on performance
        try:
            if nums[0] * N > target or nums[-1] * N < target:
                return result
        except:
            pass
        if N == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    result.append([nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while  l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            i = 0
            while i < len(nums) - (N - 1):
                result += [x + [nums[i]] for x in NSum(nums[i + 1:], N - 1, target - nums[i])]
                while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                    i += 1
                i += 1
        return result 
    return NSum_recursive(sorted(nums), N, target)
```

我们做如下主要操作

1. 对`nums`进行排序
2. 如果`N > 2`,则对每一个`nums`中的元素，我们假定它是某个解的第一个元素，并且对该元素之后的所有元素求(N-1)Sum,如果`N = 2`，则寻找2Sum

注:

1. 排序和跳过重复元素（对于连续的重复元素，我们只对第一个元素做上面的操作，这个保证了解的完整性和不重复性）保证了不会有重复元素

2. kSum的时间复杂度应该在$O(N^{k-1})$

   