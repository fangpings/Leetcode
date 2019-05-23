### 47  Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

**Example:**

```
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```

#### 想法

对于有重复元素的，我们先对列表进行排序，这样重复元素都排在一起了，然后对于每个重复元素的第一个元素，我们递归的找余下元素的permutations，再和该元素进行组合。该操作结束之后，直接跳到下一个与该元素不重复的元素。

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def rec(nums):
            if len(nums) == 1:
                return [nums]
            ret = []
            l = len(nums)
            j = 0
            while j < l:
                ret += list(map(lambda x: [nums[j]] + x, rec(nums[:j] + nums[j+1:])))
                while j < l - 1 and nums[j] == nums[j+1]:
                    j += 1
                j += 1
            return ret
        return rec(nums)
```

