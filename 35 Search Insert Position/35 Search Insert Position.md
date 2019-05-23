### 35 Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

**Example 1:**

```
Input: [1,3,5,6], 5
Output: 2
```

**Example 2:**

```
Input: [1,3,5,6], 2
Output: 1
```

**Example 3:**

```
Input: [1,3,5,6], 7
Output: 4
```

**Example 4:**

```
Input: [1,3,5,6], 0
Output: 0
```

#### 想法

带插入的二分查找

和一般二分查找差不多，只是如果不存在元素的话，最后必定会是low>high这个情况,在这之前肯定是low=high的情况，其实这个位置的下一个位置就是我们应该插入的位置，所以我们在最后直接return low就可以了

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target == []:
            return 0
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low
```

