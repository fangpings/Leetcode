### 215 Kth Largest Element in an Array

Find the **k**th largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

**Example 1:**

```
Input: [3,2,1,5,6,4] and k = 2
Output: 5
```

**Example 2:**

```
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
```

**Note:** 
You may assume k is always valid, 1 ≤ k ≤ array's length.

### 想法

和973 K Closest Points to Origin差不多。我们还是用quickselct，算法本身没什么好说的，但是很多细节真的很烦。

```python
class Solution:
    def findKthLargest(self, nums, k):
        return self.rec(nums, 0, len(nums) - 1, k)
      
    def rec(self, nums, i, j, k):
        if i == j: #不要忘了如果i==j，那么不用判断了，这个时候一定等于k
            return nums[i]
        mid = (i + j) // 2
        num_mid = nums[mid]
        old_i, old_j = i, j
        nums[mid], nums[i] = nums[i], nums[mid] #先把中间值换到最左
        i += 1 #然后i前进一格
        while i < j: #注意这个停止条件在下面两个循环都要写，否则很容易越界
            while i < j and nums[i] >= num_mid: #等于写在哪个循环都行，不影响
                i += 1
            while i < j and nums[j] < num_mid:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        #结束循环的时候i一定等于j，而且这个时候i左边的元素一定全部大于等于mid，右边的元素一定全部小于mid，但是中间的元素是不一定的，所以我们要判断一下。
        if nums[i] < num_mid:
            i -= 1
        nums[old_i], nums[i] = nums[i], nums[old_i]
        # print(i, old_i, old_j)
        if i == k - 1:
            return nums[i]
        elif i > k - 1:
            return self.rec(nums, old_i, i-1, k) # 不要忘了+1和-1
        else:
            return self.rec(nums, i+1, old_j, k)
```

记得横向对比一下binary_search是怎么写的

```python
def bs(array, target):
    if not array:
        return -1
    l, r = 0, len(array) - 1
    while l <= r: #注意这里一定是l <= r, 否则只有一个元素的数组没法处理
        mid = (l + r) // 2
        print(l, r, mid)
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1
```

需要注意的一点是，binary_seach 在

```python
while True
  if left == right:
  	return
  elif ...:
  	right = mid
  else:
  	left = mid + 1
```

这种情况下也能顺利运行