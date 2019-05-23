### 80 Remove Duplicates from Sorted Array II

Given a sorted array *nums*, remove the duplicates [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) such that duplicates appeared at most *twice* and return the new length.

Do not allocate extra space for another array, you must do this by **modifying the input array in-place** with O(1) extra memory.

**Example 1:**

```
Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
```

**Example 2:**

```
Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
```

#### 想法

一般的想法就是顺序下去然后计数，重复超过2次就remove掉。但是这个在python这里可行，c++就会显得很麻烦。换一个想法

```python
def removeDuplicates(self, nums):
    i = 0  # i代表序列中重复次数<=两次的元素个数
    for n in nums:
        if i < 2 or n > nums[i-2]:  # 前一个条件代表一开始，后一个条件代表当前元素比新列表尾端元素大，说明可以加入新的列表了。-2是因为新列表最多有两个重复元素，当末尾已经有两个重复元素的时候，第三个重复元素是没法加入的(注意i是列表尾端位置+1)。因为原列表就是顺序的，所以这里即使出现所有元素都只有一个，这个比较也是成立的，这个>唯一作用就是防止出现第三个重复元素。
            nums[i] = n
            i += 1
    return i
```